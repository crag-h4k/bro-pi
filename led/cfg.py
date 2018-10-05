from functions import reboot, hostapd_on, tor_on, scan
# ratios of .255
#2/3 = .17
#1/2 = .1275
#1/3 = .085
colors = {
    'red' : (.1, 0, 0),
    'pink' : (.066 , 0, .033), 
    'magenta' : (.05 ,0, .05), 
    'purple' : (.033, 0, .066),
    'blue' : (0, 0, .1),
    'cyan-blue' : (0, .033, .066),
    'cyan' : (0, .05, .05),
    'cyan-green' : (0, .066, 0.033),
    'green' : (0, .1, 0),
    'yellow-green' : (.033, .066, 0),
    'yellow' : (.05, .05, 0),
    'orange' : (.066, .033, 0),
    'white' : (.033, .033, .033)
    }
color_list = [
        [0, 1, 0],
        [.25, .75, 0],
        [.333, .666, 0],
        [.5, .5, 0],
        [.75, .25, 0],
        [.666, .333, 0],
        [1, 0, 0], 
        [.75, 0, .25],
        [.666 , 0, .333], 
        [.5 ,0, .5], 
        [.333, 0, .666],
        [.25, 0, .75],
        [0, 0, 1],
        [0, .25, .75],
        [0, .333, .666],
        [0, .5, .5],
        [0, .666, 0.333],
        [0, .75, .25],
       
        ]
class input_device:
    def __init__(self, pin, func, proc, color):
        self.pin  = pin
        self.func = func
        self.proc = proc
        self.color = color

reset_button = input_device(12, reboot, 'htop', 'orange')

switch_0 = input_device(26, hostapd_on, 'hostapd','white')
switch_1 = input_device(19, tor_on, 'tor', 'yellow')
switch_2 = input_device(13, scan, 'nmap', 'green')
switch_3 = input_device(6, scan, 'nmap', 'blue')
switch_4 = input_device(5, scan ,'nmap', 'purple')

red_led_pin = ['16', 'red_pin']
green_led_pin = ['20', 'green_pin']
blue_led_pin = ['21', 'blue_pin']

'''
   3V3  (1) (2)  5V    
 GPIO2  (3) (4)  5V    
 GPIO3  (5) (6)  GND   
 GPIO4  (7) (8)  GPIO14
   GND  (9) (10) GPIO15
GPIO17 (11) (12) GPIO18
GPIO27 (13) (14) GND   
GPIO22 (15) (16) GPIO23
   3V3 (17) (18) GPIO24
GPIO10 (19) (20) GND   
 GPIO9 (21) (22) GPIO25
GPIO11 (23) (24) GPIO8 
   GND (25) (26) GPIO7 
 GPIO0 (27) (28) GPIO1 
 GPIO5 (29) (30) GND   
 GPIO6 (31) (32) GPIO12
GPIO13 (33) (34) GND   
GPIO19 (35) (36) GPIO16
GPIO26 (37) (38) GPIO20
   GND (39) (40) GPIO21
'''
