import matplotlib.pyplot as plt
import pandas
import numpy

weather = pandas.read_csv('pw_file8.csv', header=None)
#print(weather)
newweather = weather.transpose()
temp = newweather[0]
#print(temp)
rain = newweather[1]
#print(rain)
wind = newweather[2]
#print(wind)
power = newweather[3]

#Plot wind:
plt.figure()
plt.subplot(4,1,1)
plt.plot(wind,'-')
plt.grid('on')
plt.xlabel('Time (min)', fontsize=16)
plt.ylabel('Wind Speed (m/s)')

#Plot temp:
plt.subplot(4,1,2)
plt.plot(temp,'-')
plt.grid('on')
plt.xlabel('Time (min)', fontsize=16)
plt.ylabel('Temperature (Kelvin)')

#Plot rain:
plt.subplot(4,1,3)
plt.plot(rain,'-')
plt.grid('on')
plt.xlabel('Time (min)', fontsize=16)
plt.ylabel('Rainfall (mm)')


#Plot power
plt.subplot(4,1,4)
plt.plot(power,'-')
plt.grid('on')
plt.xlabel('Time (min)', fontsize=16)
plt.ylabel('Power (db)')
plt.show()
