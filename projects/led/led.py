#!/usr/bin/python


from gpiozero import LED
import time

K = input("Sleep for: ")
led1 = LED(13)
led2 = LED(17)
led3 = LED(18)

while True:

	led1.toggle()
	time.sleep(K)
	led2.toggle()
	time.sleep(K)
	led3.toggle()
	time.sleep(K)
	
