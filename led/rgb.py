from time import sleep

from gpiozero import RGBLED
from cfg import colors, color_list, red_led_pin, green_led_pin, blue_led_pin

led = RGBLED(int(red_led_pin[0]), int(green_led_pin[0]), int(blue_led_pin[0])) #21,20,16
def rgb_on(color):
    led.color = colors.get(color)

def blink_led(color):
    led.color = colors.get(color)
    sleep(.25)
    led.off()
    led.color = colors.get(color)
    led.off()
    sleep(.25)
    return

def morph_colors(brightness,interval):
    while True:
        for color in color_list:
            new_color = (brightness*color[0],brightness*color[1],brightness*color[2])
            led.color = new_color
            sleep(interval)
#blink_led('cyan')
