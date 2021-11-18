import serial_utils

NO_OF_INPUTS = 8

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

def sendTrainCommand(connection,bytes):
    bytes = bytearray.fromhex('fe') + bytes
    


def ringBell():
    print("Ring bell")

def startTrain():
    print("start Train")
    
def acclerateTrain():
    print("acclerate Train")

def moveTrain():
    print("move train")
 
def decelerateTrain():
    print("decelerate Train")

def stopTrain():
    print("stop Train")

