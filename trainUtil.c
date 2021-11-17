#include "trainUtil.h"

char com_port[] = "";
uint32_t baud_rate = 9600;

HANDLE connection;

void setup() { 
    connection = open_serial_port(com_port, baud_rate); 
}


void handleInput(int input) {
    switch (input) {
        case RING_BELL:
            ringBell();
        case START_TRAIN:
            startTrain();
        case ACCLERATE_TRAIN:
            acclerateTrain();
        case MOVE_TRAIN:
            moveTrain();
        case DECELERATE_TRAIN:
            decelerateTrain();
        case STOP_TRAIN:
            stopTrain();
        case SEND_BYTE:
            readAndSendByte();
    }
}

void ringBell() {}
void startTrain() {}
void acclerateTrain() {}
void moveTrain() {}
void decelerateTrain() {}
void stopTrain() {}
void readAndSendByte() {}

