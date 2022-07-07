import paho.mqtt.client as mqtt
import requests
import json
import datetime


def on_connect(client, userdata, flags, rc):
    client.subscribe("rooms/shedhalle", qos=0)
    client.subscribe("rooms/shedhalle/humidity", qos=0)


def on_message(client, userdata, msg):
    print(msg.payload.decode())
    msg_decoded = msg.payload.decode("utf-8")
    msg_json = json.loads(msg_decoded)
    timestamp = datetime.datetime.utcnow()
    body1 = {
        "measurement": "temperature",
        "time": str(timestamp),
        "celsius": float(msg_json["temperature"])
    }

    # INFLUXDB_CLIENT.write_points(body)
    print(msg_json["pressure"])
    responseTemp = requests.post("http://127.0.0.1:8000/temp?newTemp=" + str(msg_json["temperature"]),
                                 data={"test": "test"})
    responsePressure = requests.post("http://127.0.0.1:8000/pressure?newPressure=" + str(msg_json["pressure"]),
                                     data={"test": "test"})
    responseHum = requests.post("http://127.0.0.1:8000/hum?newHum=" + str(msg_json["humidity"]), data={"test": "test"})

    print(responseTemp)
    print(responsePressure)
    print(responseHum)
    # requests.get('http://127.0.0.1:8000/')


MQTT_IP_ADDRESS = '127.0.0.1'
MQTT_USER = "ioeuser"
MQTT_PASSWORD = "2020"
MQTT_CLIENT = mqtt.Client("MQTT_PYTHON")
MQTT_CLIENT.on_connect = on_connect
# MQTT_CLIENT.on_message = on_message
MQTT_CLIENT.message_callback_add("rooms/shedhalle", on_message)
MQTT_CLIENT.username_pw_set(username=MQTT_USER, password=MQTT_PASSWORD)
MQTT_CLIENT.connect(MQTT_IP_ADDRESS, 1883, 60)
MQTT_CLIENT.loop_forever()
