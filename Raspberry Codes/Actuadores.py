from gpiozero import Servo
from gpiozero import LED
from gpiozero import Buzzer
from time import sleep
import paho.mqtt.client as mqtt
import json

class Actuadores:
    def __init__(self):
        
        self.buzzer = Buzzer(24) #El numero dentro de () indica el numero de gpio que se usa
        self.led = LED(27)
        self.servo = Servo(12)
        self.client = mqtt.Client()
        self.id = -1
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        print("connected with result code " + str(rc))
        self.client.subscribe("topic/actuador")
        
    def on_message(self, client, userdata, msg):
        json_body = json.loads(msg.payload.decode())
        self.id = json_body["id"]
        self.client.disconnect()

    def run(self):
        self.buzzer.off()
        self.led.off()
        self.servo.min()
        while True:
            self.client.connect("10.15.185.172", 1883, 60)
            
            
            
            self.client.loop_forever()
            
            if(self.id==0):
                self.buzzer.on()
                sleep(2)
                self.buzzer.off()
        
            elif(self.id==1):
                self.led.on()
                sleep(2)
                self.led.off()
            
            elif(self.id==2):
                self.servo.min()
                sleep(1)
                self.servo.max()
                sleep(1)

                self.servo.min()
        
            else:
                self.buzzer.off()
                self.led.off()
                self.servo.min()
        
        


