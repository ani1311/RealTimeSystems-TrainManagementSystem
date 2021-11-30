import serial

def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')
def getConnection(comPort,baudRate):
    return serial.Serial(comPort, baudRate)

def sendByte(connection,bytes):
    connection.write(bytes)
