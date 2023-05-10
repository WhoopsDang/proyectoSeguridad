import sys
import Adafruit_DHT
import time
import json
import paho.mqtt.client as mqtt

class sensorHumedad:
    def __init__(self, model, gpio):
        self.model = model
        self.gpio = gpio
        self.sensor = Adafruit_DHT.DHT11
        self.client = mqtt.Client()
        self.res = {"id": 1, "humedad":0,"max_humedad":25, "min_humedad":15, "tiempo":"0" }

    
    def read(self):
        while True:
            self.client.connect("localhost", 1883, 60)
            humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.gpio)
            print("Hum={0:0.1f}%".format(humidity))
            self.res["humedad"] = humidity
            res_json = json.dumps(self.res)
            self.client.publish("topic/humid", res_json)
            self.client.disconnect()
            time.sleep(2)
            








    
