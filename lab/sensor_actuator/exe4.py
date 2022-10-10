import time
from counterfit_shims_seeed_python_dht import DHT
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_led import GroveLed 

CounterFitConnection.init('127.0.0.1', 5050)

# define humidity sensor and light sensor
sensor = DHT("11", 5)
# define led
led = GroveLed(7)

while True:
    # humi as humidity, temp as temperature
    humi, temp = sensor.read()
    # print both temperature and humidity on console to check whether led achieves planned outcomes
    print(f'Temperature {temp}°C')
    print(f'Humidity {humi}%')
    if humi < 30 or humi > 60 or temp < 15 or temp > 35:
        led.on()
        print("LED is on")
    else:
        led.off()
        print("LED is off")
    time.sleep(5)
