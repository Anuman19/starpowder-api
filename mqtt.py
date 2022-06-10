import paho.mqtt.client as mqtt
import requests


def on_connect(client, userdata, flags, rc):
    client.subscribe("rooms/shedhalle")

def on_message(client, userdata, msg):
    msg_decoded = msg.payload.decode("utf-8")
    msg_json = json.loads(msg_decoded)
    timestamp = datetime.datetime.utcnow()
    body = [
        {
            "measurement": "temperature",
            "time": timestamp,
            "fields": {
                "celsius": float(msg_json["temperature"])
            }
        }
    ]
    # INFLUXDB_CLIENT.write_points(body)
    requests.post('http://127.0.0.1:8000/temp/', data=body)
    requests.get('http://127.0.0.1:8000/')


MQTT_IP_ADDRESS = '127.0.0.1'
MQTT_USER = "ioeuser"
MQTT_PASSWORD = "2020"
MQTT_CLIENT = mqtt.Client("MQTT_PYTHON")
MQTT_CLIENT.on_connect = on_connect
MQTT_CLIENT.on_message = on_message
MQTT_CLIENT.username_pw_set(username=MQTT_USER, password=MQTT_PASSWORD)
MQTT_CLIENT.connect(MQTT_IP_ADDRESS, 1883, 60)
MQTT_CLIENT.loop_forever()
