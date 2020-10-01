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

## First Steps ##
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
will be using. This will take a few moments. 

You are ready to go once your screen shows **"Your experiment is ready!"** 

