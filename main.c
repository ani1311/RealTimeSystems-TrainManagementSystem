 
/** #include <windows.h> */
#include <stdio.h>
#include "uiUtils.h" 

int main() {
    int input = 0;
    while(input != EXIT){
        input = printMenuAndTakeNextInput();
    }
}

