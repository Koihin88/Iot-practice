import time
import json
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.adc import ADC
from counterfit_shims_grove.grove_relay import GroveRelay
import paho.mqtt.client as mqtt

CounterFitConnection.init("127.0.0.1", 5050)

adc = ADC()
relay = GroveRelay(5)

id = 'e86ae430-698c-4d79-ad3f-cf531a6cbb1d'
client_name = id + 'soilmoisturesensor_client'
client_telemetry_topic = id + '/telemetry'
server_command_topic = id + '/commands'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()

def handle_command(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)

    if payload['relay_on']:
        relay.on()
    else:
        relay.off()

mqtt_client.subscribe(server_command_topic)
mqtt_client.on_message = handle_command

while True:
    soil_moisture = adc.read(0)
    print("Soil moisture:", soil_moisture)

    mqtt_client.publish(client_telemetry_topic, json.dumps({'soil_moisture' : soil_moisture}))

    time.sleep(10)
