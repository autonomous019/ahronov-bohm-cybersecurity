import pandas as pd

#format_js_data (string, list) creates js variables to hold data
def format_js_data(sensor_location, sensor_list):
  sensor_list_text = "\n\n var " + sensor_location + " = ["
  listToStr = ','.join(map(str, sensor_list)) #convert list to string using map
  sensor_list_text = sensor_list_text + listToStr + "]"
  #print(sensor1_text)
  return sensor_list_text

#import eeg data from csv then push to js script file, col_list is eeg sensor name
col_list = ["AF3","AF4","F3","F4","F7","F8","FC5","FC6","O1","O2","P7","P8","T7","T8"]
df = pd.read_csv("sample_data.csv", usecols=col_list)
#df = pd.read_csv("S01G1AllChannels.csv", usecols=col_list)

sensor1 = df["AF3"].tolist()
sensor2 = df["AF4"].tolist()
sensor3 = df["F3"].tolist()
sensor4 = df["F4"].tolist()
sensor5 = df["F7"].tolist()
sensor6 = df["F8"].tolist()
sensor7 = df["FC5"].tolist()
sensor8 = df["FC6"].tolist()
sensor9 = df["O1"].tolist()
sensor10 = df["O2"].tolist()
sensor11 = df["P7"].tolist()
sensor12 = df["P8"].tolist()
sensor13 = df["T7"].tolist()
sensor14 = df["T8"].tolist()

sensor1_text = format_js_data('AF3', sensor1)
sensor2_text = format_js_data('AF4', sensor2)
sensor3_text = format_js_data('F3', sensor3)
sensor4_text = format_js_data('F4', sensor4)
sensor5_text = format_js_data('F7', sensor5)
sensor6_text = format_js_data('F8', sensor6)
sensor7_text = format_js_data('FC5', sensor7)
sensor8_text = format_js_data('FC6', sensor8)
sensor9_text = format_js_data('O1', sensor9)
sensor10_text = format_js_data('O2', sensor10)
sensor11_text = format_js_data('P7', sensor11)
sensor12_text = format_js_data('P8', sensor12)
sensor13_text = format_js_data('T7', sensor13)
sensor14_text = format_js_data('T8', sensor14)

time_markers = [] #this is the total entries per sensor as a list

incremental_counter = df["AF3"].tolist()

for i in range(len(incremental_counter)):
    time_markers.append(i+1)

time_markers_text = format_js_data('time_markers', time_markers)

sensor_file_text = sensor1_text + sensor2_text + sensor3_text + sensor4_text + sensor5_text + sensor6_text + sensor7_text + sensor8_text + sensor9_text + sensor10_text + sensor11_text + sensor12_text + sensor13_text + sensor14_text + time_markers_text

with open('data_wrangler.js', 'w') as f:
    f.write(sensor_file_text)
