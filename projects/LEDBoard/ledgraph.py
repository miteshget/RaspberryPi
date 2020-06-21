#!/usr/bin/python


from __future__ import division
from gpiozero import LEDBarGraph
from signal import pause
from time import sleep

graph = LEDBarGraph(12, 13, 16, 17, 18, 19, 20, 21)

while True:
    graph.value = 1     #(1,1,1,1, 1,1,1,1) 
    sleep(1)
    graph.value = 1/4   #(1,1,1,1, 0,0,0,0)
    sleep(1)
    graph.value = 1/3   #(1,0,0,0,  0,0,0,0)
    sleep(1)
    graph.value = 1   #(1,0,0,0,  0,0,0,0)
    sleep(1)
    graph.value = 0     #(0,0,0,0, 0,0,0,0)
    sleep(1)
    graph.value = -1/4
    sleep(1)
    graph.value = -1/2
    sleep(1)
    graph.value = 1/204
    sleep(1)
