
import serial
serialport = "/dev/ttyACM0"
ser = serial.Serial(serialport)

def setSpeed(speed):
    if speed > 0:
        commandByte = chr(0x85)
    else:
        speed = -speed
        commandByte = chr(0x86)
    Byte1 = chr(speed & 0x1F)
    Byte2 = chr((speed >> 5) & 0x7F)
    command = commandByte + Byte1 + Byte2
    safestart = chr(0x83)
    ser.write(safestart)
    ser.write(command)
    
    
setSpeed(-1600)
