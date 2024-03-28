import time

import serial

cnt = 0
ser = serial.Serial("/dev/tty.usbserial-54790115271", 9600)
while True:
    try:
        time.sleep(1)
        cnt += 1
        ser.write(f"{cnt},{cnt*0.5}\n".encode())
        print(f"Sending '{cnt},{cnt*0.5}'")
    except KeyboardInterrupt:
        ser.close()
        break
