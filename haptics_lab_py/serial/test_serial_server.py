import time

import serial

cnt = 0

### Open serial port
ser = serial.Serial("/dev/tty.usbserial-9999", 9600, timeout=0.01)

while True:
    try:
        time.sleep(0.1)
        cnt += 1

        ### Send data to Arduino
        ser.write(f"{cnt},{cnt*0.5}\n".encode())
        print(f"Sending: {cnt}, {cnt*0.5}")

        ### Receive data from Arduino
        recv_data = ser.readline()
        if recv_data:
            _recv_data = recv_data.decode().strip().split(",")
            recv_data_1 = int(_recv_data[0])
            recv_data_2 = float(_recv_data[1])
            print(f"Received: {recv_data_1}, {recv_data_2}")

    except KeyboardInterrupt:
        ser.close()
        break
