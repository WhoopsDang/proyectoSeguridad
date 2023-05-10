import RPi.GPIO as GPIO
import time
import json
import paho.mqtt.client as mqtt


class SmokeGasSensor:
    def __init__(self, input_pin):
        self.input_pin = input_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.input_pin, GPIO.IN)
        self.client = mqtt.Client()
        self.res = {"id": 0, "humo": False, "tiempo":"0"}
        self.act = {"id": 0, "estado": False, "comando": False}


    def setMode(self):
        GPIO.setmode(GPIO.BCM)


    def read(self):
        
        while True:
            self.client.connect("localhost", 1883, 60)
            c = False
            if GPIO.input(self.input_pin) != 1:
                self.act["estado"] = False
                time.sleep(0.1)
            if GPIO.input(self.input_pin):
                print("Smoke or Gas detected")
                self.act["estado"] = True
                c = True
                time.sleep(3)
                
            self.res["humo"] = c
            res_json = json.dumps(self.res)
            act_json = json.dumps(self.act)
            self.client.publish("topic/humo", res_json)
            self.client.publish("topic/humoAct", act_json)
            self.client.disconnect()
