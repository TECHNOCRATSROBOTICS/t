#!/usr/bin/env python3

from Adafruit_BME280 import *

from flask import Flask, render_template
app = Flask(__name__)

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
 
@app.route("/")
def index():
    degrees = round(sensor.read_temperature(), 2)
    humidity = round(sensor.read_humidity(), 2)
    hectopascals = round(sensor.read_pressure() / 100, 1)

    return render_template('t.html', degrees=degrees, humidity=humidity, hectopascals=hectopascals)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)
