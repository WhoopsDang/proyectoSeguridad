from gpiozero import Buzzer, MotionSensor
import time
import json
import paho.mqtt.client as mqtt

class PIR:
    def __init__(self, input_pin):
        self.input_pin = input_pin
        self.motion_sensor = MotionSensor(self.input_pin)
        self.client = mqtt.Client()
        self.res = {"id": 0, "mov": False, "tiempo":"0"}
        self.act = {"id": "servo", "state" : False, "comando": False}
    def connect(self):
        self.client.connect("localhost", 1883, 60)
    
    def disconnect(self):
        self.client.disconnect()

    def read(self):
        
        c = True
        if self.motion_sensor.value:
            self.act["state"] = True
        else:
            self.act["state"] = False
            c = False
        self.res["mov"] = c
        res_json = json.dumps(self.res)
        act_json = json.dumps(self.act)
        self.client.publish("topic/mov", res_json)
        self.client.publish("topic/movAct", act_json )
        return c
