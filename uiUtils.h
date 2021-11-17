#include<stdio.h>

#define RING_BELL 1
#define START_TRAIN 2
#define ACCLERATE_TRAIN 3
#define MOVE_TRAIN 4
#define DECELERATE_TRAIN 5
#define STOP_TRAIN 6
#define EXIT 7
#define SEND_BYTE 8

void printMenu();
int printMenuAndTakeNextInput();
