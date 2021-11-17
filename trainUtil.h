#ifndef TRAINUTIL_H_INCLUDED
#define TRAINUTIL_H_INCLUDED

#include "serialPortUtil.h"
#include "uiUtils.h"

void setup();

void ringBell();
void startTrain();
void acclerateTrain();
void moveTrain();
void decelerateTrain();
void stopTrain();
void readAndSendByte();

#endif

