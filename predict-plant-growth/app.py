import time
import json
from counterfit_shims_seeed_python_dht import DHT
from counterfit_connection import CounterFitConnection
import paho.mqtt.client as mqtt

CounterFitConnection.init('127.0.0.1', 5050)

id = 'aed3b057-b321-45f9-ac09-75ac1a973949'
client_name = id + 'temperature_sensor_client'
client_telemetry_topic = id + '/telemetry'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()
print("mqtt connected!")

sensor = DHT("11", 5)

while True:
    _, temp = sensor.read()
    telemety = json.dumps({'temperature' : temp})
    print('Sending Temperature telemetry ', telemety)
    mqtt_client.publish(client_telemetry_topic, telemety)
    time.sleep(5)