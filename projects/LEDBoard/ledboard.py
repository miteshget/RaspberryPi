#!/usr/bin/python


from gpiozero import LEDBoard
from signal import pause
from time import sleep

leds = LEDBoard(12, 13, 16, 17, 18, 19, 20, 21)


leds.on()
sleep(1)
leds.off()
leds.value = (1, 0, 1, 0, 1, 0, 1, 0)
sleep(1)
leds.blink()

pause()
