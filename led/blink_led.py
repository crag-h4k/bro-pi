from sys import argv
from rgb import blink_led

while True:
    blink_led(argv[1])
