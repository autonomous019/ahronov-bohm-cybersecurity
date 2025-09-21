
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(123)

# ----- AB phase-coded comm -----
I0, V, k = 1.0, 0.9, 20.0
x = np.linspace(-2*np.pi, 2*np.pi, 400)
dphi0 = 2*np.pi*(0.00)   # bit 0
dphi1 = 2*np.pi*(0.25)   # bit 1
I_ref0 = I0*(1 + V*np.cos(k*x + dphi0))
I_ref1 = I0*(1 + V*np.cos(k*x + dphi1))

def tx_bit(bit): return I0*(1 + V*np.cos(k*x + (dphi0 if bit==0 else dphi1)))
def add_noise(I, sigma): return I + rng.normal(0.0, sigma, size=I.shape)
def decide(Irx): return 0 if np.dot(Irx, I_ref0) >= np.dot(Irx, I_ref1) else 1

sigmas = np.linspace(0.0, 0.4, 21)
BER = []
Nbits = 500
for s in sigmas:
    b = rng.integers(0,2,size=Nbits)
    rx = [add_noise(tx_bit(bb), s) for bb in b]
    dec = [decide(r) for r in rx]
    BER.append(np.mean(b!=np.array(dec)))

plt.figure(figsize=(7,4))
plt.plot(sigmas, BER, marker='o')
plt.xlabel('Noise σ'); plt.ylabel('Bit Error Rate'); plt.title('AB Phase Modulation: BER vs Noise')
plt.tight_layout(); plt.savefig('/mnt/data/AB_BER_curve.png'); plt.close()

# ----- BB84 toy demo -----
def bb84(N=4000, p_eve=0.0, seed=123):
    rng = np.random.default_rng(seed)
    A_bits = rng.integers(0,2,size=N)
    A_bases = rng.integers(0,2,size=N)
    B_bases = rng.integers(0,2,size=N)
    B_results = np.zeros(N, dtype=int)
    for i in range(N):
        a_bit, a_basis, b_basis = A_bits[i], A_bases[i], B_bases[i]
        if rng.random() < p_eve:
            e_basis = rng.integers(0,2)
            e_bit = a_bit if e_basis==a_basis else rng.integers(0,2)
            if b_basis==e_basis:
                B_results[i] = e_bit
            else:
                B_results[i] = rng.integers(0,2)
        else:
            if b_basis==a_basis:
                B_results[i] = a_bit
            else:
                B_results[i] = rng.integers(0,2)
    keep = (A_bases==B_bases)
    A_key, B_key = A_bits[keep], B_results[keep]
    QBER = np.mean(A_key!=B_key) if len(A_key)>0 else 0.0
    return QBER, len(A_key), N

Ps = np.linspace(0,1.0,11)
Q = []; S = []
for p in Ps:
    q, m, N = bb84(N=4000, p_eve=p, seed=42)
    Q.append(q); S.append(m/N)

plt.figure(figsize=(7,4))
plt.plot(Ps, Q, marker='o')
plt.xlabel('Intercept–Resend probability p_eve'); plt.ylabel('QBER')
plt.title('BB84: QBER vs Eavesdropping Probability')
plt.tight_layout(); plt.savefig('/mnt/data/BB84_QBER_curve.png'); plt.close()

plt.figure(figsize=(7,4))
plt.plot(Ps, S, marker='o')
plt.xlabel('p_eve'); plt.ylabel('Sifted fraction')
plt.title('BB84: Sifted Key Fraction')
plt.tight_layout(); plt.savefig('/mnt/data/BB84_sift_fraction.png'); plt.close()

print('Saved: AB_BER_curve.png, BB84_QBER_curve.png, BB84_sift_fraction.png')
