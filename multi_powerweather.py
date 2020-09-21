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

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

temps = []
rain = []
windspeed = []
fm_power = []
bes_power = []
meb_power = []
ustar_power = []
honors_power = []
smt_power = []
den_power = []

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


def get_power():
#    ssh_recieve.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 50000000 power1')
#    ssh_recieve.run('iq_to_power.py -p ~/power1 -w 25000000 -n db_power1' )
#    subprocess.call('pscp -pw kirby -scp alliet@pc16-fort.emulab.net:~/db_power1.csv db_power1.csv')
    #subprocess.call('python tryparallel.py')
    print('get power')
    subprocess.call('python multi_testbin.py')
#    with open('fm_bin_db_power.csv', newline='') as fm_csvFile:
#        print('in get power')
#        fm_powerreader = csv.reader(fm_csvFile, quoting=csv.QUOTE_NONNUMERIC)
#        for row in fm_powerreader:
#            fm_current_power = row
#    i = len(fm_current_power)
#    index = i - 1
#    fm_power.append(fm_current_power[index])

    with open('bes_bin_db_power.csv', newline='') as bes_csvFile:
#        print('in get power')
        bes_powerreader = csv.reader(bes_csvFile, quoting=csv.QUOTE_NONNUMERIC)
        for row in bes_powerreader:
            bes_current_power = row
    i = len(bes_current_power)
    index = i - 1
    bes_power.append(bes_current_power[index])

    with open('meb_bin_db_power.csv', newline='') as meb_csvFile:
#        print('in get power')
        meb_powerreader = csv.reader(meb_csvFile, quoting=csv.QUOTE_NONNUMERIC)
        for row in meb_powerreader:
            meb_current_power = row
    i = len(meb_current_power)
    index = i - 1
    meb_power.append(meb_current_power[index])

    with open('ustar_bin_db_power.csv', newline='') as ustar_csvFile:
#        print('in get power')
        ustar_powerreader = csv.reader(ustar_csvFile, quoting=csv.QUOTE_NONNUMERIC)
        for row in ustar_powerreader:
            ustar_current_power = row
    i = len(ustar_current_power)
    index = i - 1
    ustar_power.append(ustar_current_power[index])

#    with open('honors_bin_db_power.csv', newline='') as honors_csvFile:
#        print('in get power')
#        honors_powerreader = csv.reader(honors_csvFile, quoting=csv.QUOTE_NONNUMERIC)
#        for row in honors_powerreader:
#            honors_current_power = row
#    i = len(honors_current_power)
#    index = i - 1
#    honors_power.append(honors_current_power[index])

#    with open('smt_bin_db_power.csv', newline='') as smt_csvFile:
#        print('in get power')
#        smt_powerreader = csv.reader(smt_csvFile, quoting=csv.QUOTE_NONNUMERIC)
#        for row in smt_powerreader:
#            smt_current_power = row
#    i = len(smt_current_power)
#    index = i - 1
#    smt_power.append(smt_current_power[index])

#    with open('den_bin_db_power.csv', newline='') as den_csvFile:
#        print('in get power')
#        den_powerreader = csv.reader(den_csvFile, quoting=csv.QUOTE_NONNUMERIC)
#        for row in den_powerreader:
#            den_current_power = row
#    i = len(den_current_power)
#    index = i - 1
#    den_power.append(den_current_power[index])

#    return fm_power, bes_power, meb_power, ustar_power, honors_power, smt_power, den_power
    return meb_power, bes_power, ustar_power
def writetofile(url):
    temps = get_temp(complete_url)
    rain = get_rain(complete_url)
    wind = get_wind_speed(complete_url)
    meb_power, bes_power, ustar_power = get_power()
#    fm_power, bes_power, meb_power, ustar_power, honors_power, smt_power, den_power = get_power()
#    power = [2]
    with open('pw_file6.csv', 'w', newline='') as weather_file:
        weather_writer = csv.writer(weather_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        weather_writer.writerow(temps)
        weather_writer.writerow(rain)
        weather_writer.writerow(wind)
#        weather_writer.writerow(fm_power)
#        weather_writer.writerow(bes_power)
        weather_writer.writerow(meb_power)
        weather_writer.writerow(ustar_power)
#        weather_writer.writerow(honors_power)
#        weather_writer.writerow(smt_power)
#        weather_writer.writerow(den_power)

currentTime = time.time()

while True:
    if time.time() - currentTime >= 20:
        writetofile(complete_url)
        currentTime = time.time()


#schedule.every(1).minutes.do(writetofile,complete_url)

#while True:
#    schedule.run_pending()
#    time.sleep(1)
