import RPi.GPIO as gpio
import time
import sys
from Tkinter import *
import Tkinter as tk
import tkFont

command = tk.Tk()

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(32, gpio.OUT)
    gpio.setup(36, gpio.OUT)
    gpio.setup(38, gpio.OUT)
    gpio.setup(40, gpio.OUT)

def forward(tf):
    gpio.output(32, True)
    gpio.output(36, False)
    gpio.output(38, False)
    gpio.output(40, False)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    gpio.output(32, False)
    gpio.output(36, True)
    gpio.output(38, False)
    gpio.output(40, False)
    time.sleep(tf)
    gpio.cleanup()

def turn_left(tf):
    gpio.output(32, True)
    gpio.output(36, False)
    gpio.output(38, True)
    gpio.output(40, False)
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    gpio.output(32, True)
    gpio.output(36, False)
    gpio.output(38, False)
    gpio.output(40, True)
    time.sleep(tf)
    gpio.cleanup()

def pivot_left(tf):
    gpio.output(32, False)
    gpio.output(36, True)
    gpio.output(38, True)
    gpio.output(40, False)
    time.sleep(tf)
    gpio.cleanup()

def pivot_right(tf):
    gpio.output(32, False)
    gpio.output(36, True)
    gpio.output(38, False)
    gpio.output(40, True)
    time.sleep(tf)
    gpio.cleanup()


def key_input(event):
    init()
    print 'Key:',event.char
    key_press = event.char
    sleep_time = 0.030

    if key_press.lower() == 'w':
        forward(sleep_time)
    elif key_press.lower() == 's':
        reverse(sleep_time)
    elif key_press.lower() == 'q':
        turn_left(sleep_time)
    elif key_press.lower() == 'e':
        turn_right(sleep_time)
    elif key_press.lower() == 'a':
        pivot_left(sleep_time)
    elif key_press.lower() == 'd':
        pivot_right(sleep_time)
    else:
        gpio.cleanup()

command.title("Cheq_The_Rover")
command.geometry("400x400")

turn_left1 = Button(command, text = "Q", command = turn_left, height = 2, width =8 )
turn_left1.grid(row=3, column=3) #button position turn right

forward1 = Button(command, text = "W", command = forward, height = 2, width =8 )
forward1.grid(row=3, column=4) #button position go forward

turn_right1 = Button(command, text = "E", command = turn_right, height = 2, width =8 )
turn_right1.grid(row=3 , column=5) #button position turn left

pivot_left1= Button(command, text = "A", command = pivot_left, height =2 , width = 6)  
pivot_left1.grid(row = 4, column =3 ) #button position reverse Left

reverse1= Button(command, text = "S", command = reverse, height =2 , width = 6)  
reverse1.grid(row = 4, column =4 ) #button position reverse

pivot_right1= Button(command, text = "D", command = pivot_right, height =2 , width = 6)  
pivot_right1.grid(row = 4, column = 5) #button position reverse right


command.bind('<KeyPress>', key_input)
command.mainloop()
