#Definiciones de entradas y salidas de la placa PyTrainer BASIC
#Ernesto Tolocka 2021
#www.profetolocka.com.ar/pytrainer

from dht import DHT11
from machine import Pin, ADC



#Sensor de temperatura y humedad y sensor de luz
sensorDHT = DHT11 (Pin(14)) 
sensorLDR = ADC (0)          

#Leds
ledRojo = Pin (16, Pin.OUT, value=0)
ledAmarillo = Pin (15, Pin.OUT, value=0)
ledVerde = Pin (12, Pin.OUT, value=0)

buzzer = Pin (13, Pin.OUT, value=0)

#Teclas
teclaVerde = Pin (2, Pin.IN, Pin.PULL_UP)
teclaAmarilla = Pin (0, Pin.IN, Pin.PULL_UP)

buzzer.off ()


    
    



