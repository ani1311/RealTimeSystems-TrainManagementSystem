#ifndef SERIALPORTUTIL_H_INCLUDED
#define SERIALPORTUTIL_H_INCLUDED

#include <stdint.h>
#include <stdio.h>
// #include <windows.h>

typedef int HANDLE;

void print_error(const char* context);
HANDLE open_serial_port(const char *device, uint32_t baud_rate);
int write_port(HANDLE port, uint8_t *buffer, size_t size);

#endif
