import serial
import csv
import time

ser = serial.Serial('COM8', 9600) #Arduino board port is com8
print(ser)
ser_bytes = ser.readline()

#ser.flushInput()

while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)

        #with open('test_data.csv', 'w', newline='') as csvfile:
        #   fieldnames = ['first_name', 'last_name']
        #    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #    writer = csv.writer(csvfile, delimiter=",")
        #    writer.writerow([time.time(), decoded_bytes])

        #with open("test_data.csv", "a") as f:
        #    writer = csv.writer(f, delimiter=",")
        #    writer.writerow([time.time(), decoded_bytes])
    except:
        print("Keyboard Interrupt")
        break