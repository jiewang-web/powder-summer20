# Collecting Power and Weather Measurements on the POWDER Platform #

The goal of this tutorial is to step through the process of collecting
both received signal strength and weather data within the POWDER Platform
over an undetermined and extended period of time. The received signal 
strength values are gathered between two CBRS rooftop nodes. The weather
data is collected from the Open Weather Map API. 

## Before You Begin ##
**Create a reservation** on the POWDER Platform for at least two CBRS
rooftop nodes. The nodes that you choose will be the transmitter/receiver pair
and should be chosen accordingly. 
Choose from these:
  * cbrssdr1-bes 
  * cbrssdr1-browning
  * cbrssdr1-dentistry
  * cbrssdr1-fm
  * cbrssdr1-honors
  * cbrssdr1-meb
  * cbrssdr1-smt
  * cbrssdr1-ustar
    
The **reservation should also include** the same number of either d430 or d740
compute nodes depending on resource availability. It can also be helpful to reserve 
the 3550 to 3560 frequency range. 

The weather data will be collected through the 
[Open Weather Map API](https://openweathermap.org), so you will need to **create an 
account** and receive an API key to be used for data collection.

The collection of the power and weather data will utalize both the
[powerweather_tutorial.py](https://github.com/allisontodd/powder-summer20/blob/master/tutorials/collect-power-weather/powerweather_tutorial.py)
and [rxtx_tutorial.py](https://github.com/allisontodd/powder-summer20/blob/master/tutorials/collect-power-weather/rxtx_tutorial.py)
Python scripts. Make sure that both of these are downloaded into
the directory you will to use for data collection.

## Instantiate the Experiment ##
Using the CBRS rooftops nodes reserved above, instantiate an experiment on the 
POWDER platform following these step:
  1. select **Experiments**
  2. choose **Start Experiment**
  3. select **Change Profile**
  4. find **signal_power**
  5. click **Select Profile** then **Next**
  6. choose the **Compute node type** you reserved (d740 or d430)
  7. adjust **frequency range** to match your reservation
  8. add the appropriate number of **X310 CBRS Radios** (likely 2)
  9. specify the **names** of the CBRS Radios you reserved
  10. click **Next**
  11. optionally **name** your experiment here then click **Next**
  12. select your reservation which sets the begin and end times
  13. click **Finish**
  
Now, your experiment will begin provisioning and booting up the resources you
will be using. This will take a few moments. You are ready to go once your 
screen shows **"Your experiment is ready!"** 

## Make the Changes ##
You now need to go into the Python code you downloaded earlier and alter certain
portions so that it will work for you. This requires you know 7 pieces of information:
 1. your Open Weather Map API Key 
 2. the destination file name you would like to create (.csv)
 3. the ssh password for your device
 4. your POWDER username for ssh 
 5. SSH url for transmit node
 6. SSH url for receive node
 7. location of ssh key_filename on your device

Go into both powerweather_tutorial.py and rxtx_tutorial.py and make all the appropriate
changes as specified below:

 **powerweather_tutorial.py**
  * **line 17** : add Open Weather Map API Key
  * **line 119** : add destination file name you wish to create
  
 **rxtx_tutorial.py**
  * **line 10** : add ssh password + ssh url for receive node + ssh username
  * **line 20** : add ssh url for transmit node + ssh username
  * **line 21** : add location of ssh key_filename
  * **line 24** : add ssh url for receive node + ssh username
  * **line 25** : add location of ssh key_filename
  
## Running It ##
Now that all the necessary changes have been made, the script can be run and the 
data collection can begin!

Run powerweather_tutorial.py however you prefer to run Python scripts and watch
as both recieved signal strength and weather data is collected. Data is collected 
approximately every one minute and will continue being collected until you stop
running powerweather_tutorial.py.

## The Data ##
Once you are done, the data you collected will be found in the destination 
file you named. The .csv file you created will have five rows and the number of 
columns entirely depends on the length of time the experiment was run for. 
 * **First Row** : Environmental Temperature
 * **Second Row** : Rainfall
 * **Third Row** : Windspeed
 * **Fourth Row** : Percent Humidity
 * **Fifth Row** : Received Signal Strength Value
 
 The MatLab code plot_tutorial.m is included so that you may graph the data collection.
 Be sure to change the file name on line 6 to match the destination file name used 
 previously. 
