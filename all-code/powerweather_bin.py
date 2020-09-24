import requests
import json
import csv
import pandas
import numpy
import schedule
import time
from fabric import Connection, Config
from invoke import Responder
from csv import reader, writer
import getpass
import subprocess
import matplotlib.pyplot as plt
from multiprocessing import Process

api_key = "7716dafd84df0f27a810a5b5a7310c10"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Salt Lake City"
lat = '40.765229'
lon = '-111.846208'

#complete_url = base_url + "appid=" + api_key + "&q=" + city_name
complete_url = base_url + "appid=" + api_key + "&lat=" + lat +"&lon=" + lon +"&units=metric"

temps = []
rain = []
windspeed = []
power = []
endRecieve = False

#Temperature function
def get_temp(url):
    # get method of requests module, return response object
    response = requests.get(complete_url)
    # json method of response object convert json format data into
    # python format data
    x = response.json()
    # store the value of "main", key in variable y
    y = x["main"]
    # store the value corresponding to the "temp" key of y
    current_temperature = y["temp"]
    temps.append(current_temperature)

    return temps

#Rainfall function
def get_rain(url):
    # get method of requests module, return response object
    response = requests.get(complete_url)
    # json method of response object convert json format data into
    # python format data
    x = response.json()
    # store the value of "main", key in variable y
    try:
        b = x["rain"]
    except:
        current_rain = 0
    else:
        current_rain = b["1h"]
    finally:
        rain.append(current_rain)

    return rain

#Wind speed function
def get_wind_speed(url):
    # get method of requests module, return response object
    response = requests.get(complete_url)
    # json method of response object convert json format data into
    # python format data
    x = response.json()
    # store the value of "main", key in variable y
    a = x["wind"]

    current_wind_speed = a["speed"]
    #wind_degree = a["deg"]

    windspeed.append(current_wind_speed)

    return windspeed

def get_humid(url):
    # get method of requests module, return response object
    response = requests.get(complete_url)
    # json method of response object convert json format data into
    # python format data
    x = response.json()
    # store the value of "main", key in variable y
    y = x["main"]
    # store the value corresponding to the "temp" key of y
    current_humid = y["humidity"]
    humid.append(current_humid)

    return humid


def get_power():
#    ssh_recieve.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 50000000 power1')
#    ssh_recieve.run('iq_to_power.py -p ~/power1 -w 25000000 -n db_power1' )
#    subprocess.call('pscp -pw kirby -scp alliet@pc16-fort.emulab.net:~/db_power1.csv db_power1.csv')
    #subprocess.call('python tryparallel.py')
    print('get power')
    subprocess.call('python testbin.py')
    with open('single_test_bin_db_power3.csv', newline='') as csvFile:
        powerreader = csv.reader(csvFile, quoting=csv.QUOTE_NONNUMERIC)
        for row in powerreader:
            current_power = row

    i = len(current_power)
    index = i - 1
    power.append(current_power[index])
    return power

def writetofile(url):
    temps = get_temp(complete_url)
    rain = get_rain(complete_url)
    wind = get_wind_speed(complete_url)
    humid = get_humid(complete_url)
#    get_db_file()
    power = get_power()
#    power = [2]
    with open('pw_file10.csv', 'w', newline='') as weather_file:
        weather_writer = csv.writer(weather_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        weather_writer.writerow(temps)
        weather_writer.writerow(rain)
        weather_writer.writerow(wind)
        weather_writer.writerow(humid)
        weather_writer.writerow(power)

currentTime = time.time()

while True:
    if time.time() - currentTime >= 50:
        writetofile(complete_url)
        currentTime = time.time()


#schedule.every(1).minutes.do(writetofile,complete_url)

#while True:
#    schedule.run_pending()
    #time.sleep(1)
