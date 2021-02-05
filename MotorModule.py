import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor():
    def __init__(self,In1A,In2A,In1B,In2B):
        self.In1A = In1A
        self.In2A = In2A
        self.In1B = In1B
        self.In2B = In2B
        GPIO.setup(self.In1A,GPIO.OUT)
        GPIO.setup(self.In2A,GPIO.OUT)
        GPIO.setup(self.In1B,GPIO.OUT)
        GPIO.setup(self.In2B,GPIO.OUT)

    def forward(self,t=0):
            gpio.output(self.In1A, True)
            gpio.output(self.In2A, False)
            gpio.output(self.In1B, False)
            gpio.output(self.In2B, False)
            sleep(t)
    def reverse(self,t=0):

            gpio.output(self.In1A, False)
            gpio.output(self.In2A, True)
            gpio.output(self.In1B, False)
            gpio.output(self.In2B, False)
            sleep(t)

    def turn_left(self,t=0):
            gpio.output(self.In1A, True)
            gpio.output(self.In2A, False)
            gpio.output(self.In1B, True)
            gpio.output(self.In2B, False)
            sleep(t)

    def turn_right(self,t=0):
            gpio.output(self.In1A, True)
            gpio.output(self.In2A, False)
            gpio.output(self.In1B, False)
            gpio.output(self.In2B, True)
            sleep(t)
    def pivot_left(self,t=0):
            gpio.output(self.In1A, False)
            gpio.output(self.In2A, True)
            gpio.output(self.In1B, True)
            gpio.output(self.In2B, False)
            sleep(t)
    def pivot_right(self,t=0):
            gpio.output(self.In1A, False)
            gpio.output(self.In2A, True)
            gpio.output(self.In1B, False)
            gpio.output(self.In2B, True)
            sleep(t)
    def stop(self,t=0):
          sleep(t)


motor = Motor(32,36,38,40)

while True:
    Motor.forward()
    Motor.reverse()
    Motor.turn_left()
    Motor.turn_right()
    Motor.pivot_left()
    Motor.pivot_right()
    Motor.stop(2)










