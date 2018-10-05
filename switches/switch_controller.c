//gcc switch_controller.c -l wiringPi -o switch_controller

#include <wiringPi.h>
#include <stdlib.h>
#include <stdio.h>

//BCM 
#define SHUTDOWN_PIN 12
#define AP_PIN 26 
#define BRO_PIN 19 
#define TOR_PIN 13
#define NMAP_PIN 6
#define WARMODE_PIN 5

//wPi
/*#define SHUTDOWN_PIN 26
#define AP_PIN 25
#define BRO_PIN 24
#define TOR_PIN 23
#define NMAP_PIN 22
#define WARMODE_PIN 21 
*/
void init_pin(int pin){
    //bcm mode
    wiringPiSetupGpio(); 
    //wPi
    //wiringPiSetup(); 
    pinMode(pin,INPUT);
    pullUpDnControl(pin, PUD_UP);
    
    printf("init_pin %i finished\n",pin);
}

int main(){
    int pins[6] = {SHUTDOWN_PIN, AP_PIN, BRO_PIN, TOR_PIN, NMAP_PIN, WARMODE_PIN};
    const char *commands[6] = {"shutdown now", "systemctl start hostapd", "broctl deploy","tor --quiet", "nmap 192.168.2.2-102 -Pn -sV version-all", "warmode"};

    int array_size = sizeof(pins) / sizeof(int);

    wiringPiSetupGpio(); 

    for(int i=0; i< array_size; i++){
        pinMode(pins[i],INPUT);
        pullUpDnControl(pins[i], PUD_DOWN);
        printf("init_pin %i finished\n",pins[i]);
    }

    while(1){
      for(int i=0; i< array_size; i++){
          //printf("reading pin %i\n", pins[i]);
          if (digitalRead(pins[i])){
              //printf(commands[i]);
              printf("%s executed \n\tbcm pin %i\n", commands[i], pins[i]);
              //printf("pin %i\n",pins[i]);
              //delay(250);
              //system(commands[i]);
              //continue;
          }
      }
      printf("\n");
    }
}
//gcc switch_controller.c -l wiringPi -o switch_controller

#include <wiringPi.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

//BCM 
#define PLUG_SIDE 4 
#define BLANK_SIDE 17

int main(){
    int channels[6 ] = {PLUG_SIDE, BLANK_SIDE};
    char* init_state = "0";
    char* new_state = "1";
    char* current_state = "0";

    // [command][state] state starts at 0 then changes to 1 if the switch turned on,
    // if the switch is turned off, then state will change bakc to 0
    char *commands[6][2]= {
        {"ping google.com -c 20", current_state},
        {"date +%T|xargs touch", current_state},
    };
        
    int array_size = sizeof(channels) / sizeof(int);

    wiringPiSetupGpio(); 

    for(int i=0; i< array_size; i++){
        pinMode(channels[i],INPUT);
        pullUpDnControl(channels[i], PUD_DOWN);
        printf("init_channel %i finished\n",channels[i]);
    }

    while(1){
      for(int i=0; i< array_size; i++){
          if (digitalRead(channels[i])){
              //check if already executed command
              if (commands[i][1] == init_state){
                  commands[i][1] = new_state;
                  system(commands[i][0]);
                  printf("%s executed \n\tbcm channel %i\n", commands[i][0], channels[i]);
              } else{
                  continue;
              }
          }else{
              //allows for reset of channel to original state so that the switch can execute the proper system command
              commands[i][1] == init_state;
              //printf("reset state of channel %i\n", channels[i]);
              pullUpDnControl(channels[i], PUD_DOWN);

          }
        delay(500);
      }
    //these two lines are just for testing
    //delay(250);
    //printf("\n");
    }
}
