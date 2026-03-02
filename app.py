from flask import Flask, render_template_string
import RPi.GPIO as GPIO

app = Flask(__name__)

LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

led_state = False

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>LED Control</title>
</head>
<body style="text-align:center; margin-top:100px;">
    <h1>Raspberry Pi LED Control</h1>
    <h2>LED is {{ state }}</h2>
    <a href="/toggle">
        <button style="padding:15px 30px; font-size:20px;">Toggle LED</button>
    </a>
</body>
</html>
"""

@app.route('/')
def home():
    global led_state
    return render_template_string(HTML_PAGE, state="ON" if led_state else "OFF")

@app.route('/toggle')
def toggle():
    global led_state
    led_state = not led_state
    GPIO.output(LED, led_state)
    return render_template_string(HTML_PAGE, state="ON" if led_state else "OFF")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
