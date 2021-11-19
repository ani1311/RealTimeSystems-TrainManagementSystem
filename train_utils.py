import serial_utils

NO_OF_INPUTS = 8

COM_PORT = "COM1"
BAUD_RATE = 9600

FIRST_BYTE_OF_COMMAND = "11111110"
ENGINE_ID = "000010111"

connection = serial_utils.getConnection(COM_PORT,BAUD_RATE)

def printMenu():
    print("Train Management System Options:");
    print("1) Ring bell");
    print("2) Start train");
    print("3) Acclerate train");
    print("4) Move train");
    print("5) Decelerate train");
    print("6) Stop train");
    print("7) Exit");

def displayMenuAndTakeInput():
    printMenu()
    ip = int(input())
    while(ip < 1 or ip > 7):
        print("Wrong input: {0}, try again".format(ip))
        ip = int(input())
    return ip

def handleInput(input):
    match input:
        case 1:
            ringBell()
        case 2:
            startTrain()
        case 3:
            acclerateTrain()
        case 4:
            moveTrain()
        case 5:
            decelerateTrain()
        case 6:
            stopTrain()

def sendTrainCommand(data):
    hexData = serial_utils.bitstring_to_bytes(FIRST_BYTE_OF_COMMAND + ENGINE_ID + data)
    connection.write(hexData)

def ringBell():
    COMMAND = "00"
    DATA = "11101"
    sendTrainCommand(COMMAND + DATA)

## set Absolute speed to 8
def startTrain():
    COMMAND = "11"
    DATA = "01000"
    sendTrainCommand(COMMAND + DATA)

## Increase relaitive speed by 3 
def acclerateTrain():
    COMMAND = "10"
    DATA = "01000"
    sendTrainCommand(COMMAND + DATA)

## Same as start
def moveTrain():
    startTrain()
 
## Decrease relaitive speed by 3 
def decelerateTrain():
    COMMAND = "10"
    DATA = "00010"
    sendTrainCommand(COMMAND + DATA)

## Set absolute speed to 0
def stopTrain():
    COMMAND = "11"
    DATA = "00000"
    sendTrainCommand(COMMAND + DATA)
