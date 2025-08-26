#!/usr/bin/env python3
"""
Fetch daily space-weather indices (Kp, Dst, AE) and local dB/dt and log them to a CSV.
- Kp: NOAA SWPC 1-minute planetary K index (latest value)
- Dst: Kyoto WDC real-time Dst (hourly; last available hour)
- AE:  Kyoto WDC real-time AE (1-min; last available minute)
- dB/dt: Computed from USGS Geomag 1-minute data (station default FRD - Fredericksburg, VA)
         as the max absolute |dH/dt| over the local day (UTC by default)

Usage:
  python fetch_spaceweather_to_csv.py --csv autism_geomagnetic_study_template.csv --station FRD --tz UTC
  (station choices commonly available via USGS: FRD, BOU, SJG, HON, TUC, FRN)
  For Portland, ME, FRD is a reasonable East Coast proxy. If you prefer Canada (OTT), you will need NRCan APIs.
"""
import argparse
import datetime as dt
import json
import sys
from typing import Optional

import pandas as pd
import requests

# ---------- Configuration ----------
Kp_URL = "https://services.swpc.noaa.gov/json/planetary_k_index_1m.json"  # 1-min estimated Kp
# Kyoto Dst realtime monthly HTML table (we'll parse the last numeric)
Kyoto_DST_URL = "https://wdc.kugi.kyoto-u.ac.jp/dst_realtime/presentmonth/index.html"
# Kyoto AE realtime monthly HTML table
Kyoto_AE_URL = "https://wdc.kugi.kyoto-u.ac.jp/ae_realtime/presentmonth/index.html"

# USGS Geomag Web Service docs: https://geomag.usgs.gov/ws/
USGS_BASE = "https://geomag.usgs.gov/ws/data/"
USGS_ELEMENTS = "H"  # we'll fetch H (horizontal intensity) to compute dH/dt

def fetch_latest_kp() -> Optional[float]:
    try:
        r = requests.get(Kp_URL, timeout=15)
        r.raise_for_status()
        data = r.json()
        if not data:
            return None
        last = data[-1]
        # Fields: time_tag, kp_index (float), observed/reported booleans
        return float(last.get("kp_index"))
    except Exception as e:
        print(f"[warn] Kp fetch failed: {e}", file=sys.stderr)
        return None

def _parse_last_number_from_tables(url: str) -> Optional[float]:
    try:
        tables = pd.read_html(url)
        # scan from last to first; pick the last numeric-looking cell
        for tbl in reversed(tables):
            vals = pd.to_numeric(tbl.applymap(lambda x: str(x).strip()).stack(), errors="coerce")
            vals = vals.dropna()
            if len(vals):
                return float(vals.iloc[-1])
        return None
    except Exception as e:
        print(f"[warn] parse tables failed ({url}): {e}", file=sys.stderr)
        return None

def fetch_latest_dst() -> Optional[float]:
    # Returns last available Dst (nT)
    return _parse_last_number_from_tables(Kyoto_DST_URL)

def fetch_latest_ae() -> Optional[float]:
    # Returns last available AE (nT)
    return _parse_last_number_from_tables(Kyoto_AE_URL)

def fetch_usgs_1min(station: str, start: dt.datetime, end: dt.datetime) -> Optional[pd.DataFrame]:
    # station examples: FRD, BOU, SJG, HON, TUC, FRN
    # API params
    params = {
        "id": station,
        "format": "json",
        "type": "variation",         # 1-minute variation data
        "elements": USGS_ELEMENTS,
        "sampling_period": 60,       # seconds
        "starttime": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "endtime": end.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "include_headers": "true",
    }
    try:
        r = requests.get(USGS_BASE, params=params, timeout=30)
        r.raise_for_status()
        payload = r.json()
        # Expect: {"status": {"code": ...}, "units": {...}, "data": [{"time": "...", "H": value}, ...]}
        if "data" not in payload:
            return None
        df = pd.DataFrame(payload["data"])
        # Convert time to pandas datetime
        df["time"] = pd.to_datetime(df["time"], utc=True)
        # Ensure H is numeric
        df["H"] = pd.to_numeric(df["H"], errors="coerce")
        df = df.dropna(subset=["H"])
        return df
    except Exception as e:
        print(f"[warn] USGS fetch failed: {e}", file=sys.stderr)
        return None

def compute_db_dt(df: pd.DataFrame) -> Optional[float]:
    """Compute max absolute dH/dt (nT/min) over the period."""
    try:
        df = df.sort_values("time")
        # difference in H (nT) per minute
        dH = df["H"].diff()
        # since sampling is 1 min, dH per minute already
        max_abs = dH.abs().max()
        if pd.isna(max_abs):
            return None
        return float(max_abs)
    except Exception as e:
        print(f"[warn] dB/dt compute failed: {e}", file=sys.stderr)
        return None

def upsert_row(csv_path: str, date_str: str, kp: Optional[float], dst: Optional[float], ae: Optional[float], dbdt: Optional[float]):
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        # Initialize a new sheet following the template
        cols = ["date","symptom_score","notes","sleep_hours","sleep_quality","HRV_rmssd","meds_changes","weather_temp","weather_pressure","Kp_index","Dst_index","AE_index","dB_dt_local"]
        df = pd.DataFrame(columns=cols)

    if "date" not in df.columns:
        df["date"] = []

    if (df["date"] == date_str).any():
        idx = df.index[df["date"] == date_str][0]
    else:
        idx = len(df)
        df.loc[idx, "date"] = date_str

    # Only overwrite indices if fetched (non-None)
    if kp is not None:
        df.loc[idx, "Kp_index"] = kp
    if dst is not None:
        df.loc[idx, "Dst_index"] = dst
    if ae is not None:
        df.loc[idx, "AE_index"] = ae
    if dbdt is not None:
        df.loc[idx, "dB_dt_local"] = dbdt

    df.to_csv(csv_path, index=False)
    return df

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True, help="Path to your daily CSV (from the template)")
    ap.add_argument("--station", default="FRD", help="USGS station for dB/dt (FRD, BOU, SJG, HON, TUC, FRN...)")
    ap.add_argument("--tz", default="UTC", help="Time zone for 'day' definition; use 'UTC' or 'local'. Affects dB/dt window.")
    args = ap.parse_args()

    now_utc = dt.datetime.utcnow()
    if args.tz.upper() == "LOCAL":
        # define "day" as local midnight to now; approximate using local time
        today_local = dt.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        start = today_local.astimezone(dt.timezone.utc).replace(tzinfo=None)
        end = now_utc
        date_str = today_local.date().isoformat()
    else:
        # UTC day
        start = now_utc.replace(hour=0, minute=0, second=0, microsecond=0)
        end = now_utc
        date_str = start.date().isoformat()

    print(f"[info] Fetching indices for {date_str} (UTC window {start} to {end}) ...")

    kp = fetch_latest_kp()
    print(f"[info] Kp: {kp}")

    dst = fetch_latest_dst()
    print(f"[info] Dst: {dst} nT")

    ae = fetch_latest_ae()
    print(f"[info] AE: {ae} nT")

    df_usgs = fetch_usgs_1min(args.station.upper(), start, end)
    if df_usgs is not None and not df_usgs.empty:
        dbdt = compute_db_dt(df_usgs)
    else:
        dbdt = None
    print(f"[info] dB/dt (max |dH/dt|): {dbdt} nT/min (station {args.station.upper()})")

    df_out = upsert_row(args.csv, date_str, kp, dst, ae, dbdt)
    print(f"[ok] Updated {args.csv} with space-weather indices.")
    # Optional: print last few rows
    print(df_out.tail())

if __name__ == "__main__":
    main()
