import serial
import time
arduino = serial.Serial("COM4", 9600)
time.sleep(2)
i = 1
while(i > 0):
    dato = input(
        "Presiona s si deseas encender el led \n Presiona n si deseas apagar")
    time.sleep(1)
    arduino.write(dato.encode())
    if(dato == "n"):
        i = 0
arduino.close()
