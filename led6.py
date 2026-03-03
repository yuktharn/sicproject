import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

# ---------- GPIO Setup ----------
GPIO.setmode(GPIO.BCM)
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

# ---------- MQTT Settings ----------
BROKER_IP = "192.168.6.132"   # 🔴 CHANGE THIS to your broker IP
TOPIC = "led/control"

# ---------- When Message Received ----------
def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print("Received:", message)

    if message == "ON":
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED ON")

    elif message == "OFF":
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED OFF")

# ---------- MQTT Client ----------
client = mqtt.Client()
client.on_message = on_message

client.connect(BROKER_IP, 1883, 60)
client.subscribe(TOPIC)

print("Waiting for MQTT messages...")
client.loop_forever()
