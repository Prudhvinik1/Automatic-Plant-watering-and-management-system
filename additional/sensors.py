import requests, json
import Adafruit_DHT
import sys, mcp3008
import motor
import time
from ultra_sonic_sensor import get_distance
from motor import run_motor
bucket = 70
while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    moisture = mcp3008.readadc(5)
    distance = get_distance()
    distance = (1-distance/bucket)*100
    print(humidity,temperature,moisture,distance)
    
    #run_motor(moisture)
    
    '''url = 'http://127.0.0.1:8100/weather/json/'
    payload = {'data':str(temperature) + ', ' + str(humidity) + ', ' + str(moisture) + ", " + str(distance)}
    r = requests.post(url,data = payload)'''
    time.sleep(2)
