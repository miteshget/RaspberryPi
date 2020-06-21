#!/usr/bin/python


from gpiozero import Button
from gpiozero import LED
from signal import pause
import time

button = Button(27)
blue = LED(16)
red = LED(17)
green = LED(18)

def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")

def turn_on_led():
    blue.toggle()
    time.sleep(.5)
    red.toggle()
    time.sleep(.5)
    green.toggle()
    time.sleep(.5)


# button.when_pressed = say_hello
# button.when_released = say_goodbye
button.when_pressed = turn_on_led

pause()




