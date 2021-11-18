import serial

def getConnection(comPort,baudRate):
    return serial.Serial(comPort, baudRate)

def sendByte(connection,bytes):
    connection.write(bytes)
