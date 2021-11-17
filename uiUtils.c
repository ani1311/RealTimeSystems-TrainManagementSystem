#include "uiUtils.h"

void printMenu() {
    printf("Train Management System Options:\n");
    printf("%d) Ring bell\n",RING_BELL);
    printf("%d) Start train\n",START_TRAIN);
    printf("%d) Acclerate train\n",ACCLERATE_TRAIN);
    printf("%d) Move train\n",MOVE_TRAIN);
    printf("%d) Decelerate train\n",DECELERATE_TRAIN);
    printf("%d) Stop train\n",STOP_TRAIN);
    printf("%d) Exit\n",EXIT);
}

int printMenuAndTakeNextInput() {
    printMenu();
    int input;
    scanf("%d",&input);
    while(input < 1 || input > 8){
        printf("Invalid input %d, Give proper input\n",input);
        scanf("%d",&input);
    }
    return input;
}

