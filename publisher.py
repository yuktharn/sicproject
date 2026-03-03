import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO

# MQTT Setup
BROKER = "localhost"
PORT = 1883
TOPIC = "lab/device/control"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

# Ultrasonic Sensor Pins
TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print("Starting Real Distance Publisher... (Ctrl+C to stop)")

try:
    while True:
        # Send trigger pulse
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        # Wait for echo start
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        # Wait for echo end
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        # Distance calculation
        distance = pulse_duration * 17150
        distance = round(distance, 2)

        message = f"Distance: {distance} cm"

        client.publish(TOPIC, message)
        print("Published:", message)

        time.sleep(1)

except KeyboardInterrupt:
    print("Publisher stopped.")
    GPIO.cleanup()

