import matplotlib.pyplot as plt
import pandas
import numpy

weather = pandas.read_csv('pw_file2.csv', header=None)
#print(weather)
newweather = weather.transpose()
temp = newweather[0]
#print(temp)
rain = newweather[1]
#print(rain)
wind = newweather[2]
#print(wind)
fm_power = newweather[3]

bes_power = newweather[4]

meb_power = newweather[5]

ustar_power = newweather[6]

honors_power = newweather[7]

smt_power = newweather[8]

den_power = newweather[9]

#Plot wind:
plt.figure()
plt.subplot(10,1,1)
plt.plot(wind,'-')
plt.grid('on')
plt.xlabel('Time (min)', fontsize=16)
plt.ylabel('Wind Speed (m/s)')

#Plot temp:
plt.subplot(10,1,2)
plt.plot(temp,'-')
plt.grid('on')
plt.xlabel('Time (min)', fontsize=16)
plt.ylabel('Temperature (Kelvin)')

#Plot rain:
plt.subplot(10,1,3)
plt.plot(rain,'-')
plt.grid('on')
plt.xlabel('Time (min)', fontsize=16)
plt.ylabel('Rainfall (mm)')


#Plot power
plt.subplot(10,1,4)
plt.plot(fm_power,'-')
plt.grid('on')
plt.xlabel('Time (min)', fontsize=16)
plt.ylabel('Power (db)')


plt.subplot(10,1,5)
plt.plot(bes_power,'-')
plt.grid('on')
plt.xlabel('Time (min)', fontsize=16)
plt.ylabel('Power (db)')


plt.subplot(10,1,6)
plt.plot(meb_power,'-')
plt.grid('on')
plt.xlabel('Time (min)', fontsize=16)
plt.ylabel('Power (db)')


plt.subplot(10,1,7)
plt.plot(ustar_power,'-')
plt.grid('on')
plt.xlabel('Time (min)', fontsize=16)
plt.ylabel('Power (db)')


plt.subplot(10,1,8)
plt.plot(honors_power,'-')
plt.grid('on')
plt.xlabel('Time (min)', fontsize=16)
plt.ylabel('Power (db)')


plt.subplot(10,1,9)
plt.plot(smt_power,'-')
plt.grid('on')
plt.xlabel('Time (min)', fontsize=16)
plt.ylabel('Power (db)')


plt.subplot(10,1,10)
plt.plot(den_power,'-')
plt.grid('on')
plt.xlabel('Time (min)', fontsize=16)
plt.ylabel('Power (db)')
plt.show()
