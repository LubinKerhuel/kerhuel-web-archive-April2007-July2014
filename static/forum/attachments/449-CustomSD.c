#include <p32xxxx.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "FSconfig.h"
#include "HardwareProfile.h"
#include "GenericTypeDefs.h"
#include "FSIO.h"

#define NumRetries 10

FSFILE * filePtr;


unsigned char FS_init_loop(void){
    unsigned char i;
    for (i=0; i < NumRetries; i++){
    if(FSfinit()==0)  return 1;
    return 0;    
    }
}

unsigned char FSopen(char *u1){
    filePtr = FSfopen( u1,FS_WRITE);
    if (filePtr != NULL) {
        return 1;
    }
    else return 0;  
}

void FSclose(void){
    FSfclose(filePtr);
}

unsigned char FSprint(unsigned int u1){
    char y1;
    y1 = FSfprintf(filePtr, "AN0= %u%c%c", u1, 0x0D, 0x0A);
    if (y1 > 0){
        return 1;
    }
    else return 0;
}
