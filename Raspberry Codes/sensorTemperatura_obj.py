import sys
import Adafruit_DHT
import time
import json
import paho.mqtt.client as mqtt

class sensorTemperatura:
    def __init__(self, model, gpio):
        self.model = model
        self.gpio = gpio
        self.sensor = Adafruit_DHT.DHT11
        self.client = mqtt.Client()
        self.res = {"id": 1, "temperatura": 0, "max_temp": 40, "min_temp":-1, "tiempo":"0" }

    
    def read(self):
        while True:
            self.client.connect("localhost", 1883, 60)
            humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.gpio)
            print("Temp={0:0.1f}C".format(temperature))
            self.res["temperatura"] = temperature
            res_json = json.dumps(self.res)
            self.client.publish("topic/temp", res_json)
            self.client.disconnect()
            time.sleep(2)
            


