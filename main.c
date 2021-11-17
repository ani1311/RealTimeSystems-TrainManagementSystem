 
/** #include <windows.h> */
#include <stdio.h>
#include "trainUtil.h" 

int main() {
    int input = 0;
    while(input != EXIT){
        input = printMenuAndTakeNextInput();
    }
}

