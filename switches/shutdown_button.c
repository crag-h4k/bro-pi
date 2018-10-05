// thank you to github user rricharz
#include <wiringPi.h>
#include <stdio.h>

#define PIN 12

int main(int argc,char **argv){
    printf("listening pin %i for shudown/n", PIN);
    wiringPiSetup();
    pinMode(PIN,INPUT);
    pullUpDnControl(PIN, PUD_UP);

    do {
        if(digitalRead(PIN) == 0){
            printf("shutdown input recieved..\n");
            system("shutdown -h now");
            }
        delay(1000);
    }
    while(1);

}
