import RPi.GPIO as gpio
import time
import mcp3008

def run_motor(moisture):
    gpio.setmode(gpio.BCM)
    gpio.setup(20,gpio.OUT)
    if(moisture>600):
        gpio.output(20,gpio.HIGH) 
    else:
        gpio.output(20,gpio.LOW)
    time.sleep(2)
    return 
    
  
 
