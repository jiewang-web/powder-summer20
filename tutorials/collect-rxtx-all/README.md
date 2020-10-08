# Collecting Recieved Signal Strength between all combinations of Transmitters and Receivers #

The goals of this tutorial is to step through the process of collecting received signal
strength measurements between all combinations of transmitter and receivers within the
POWDER Platform. The data is collected between all available CBRS rooftop nodes. 

## Before You Begin ##
**Create a reservation** on the POWDER Platform for all available CBRS rooftop nodes. At
the moment, the tutorial supports the following CBRS nodes:
 * cbrssdr1-bes
 * cbrssdr1-browning
 * cbrssdr1-dentistry
 * cbrssdr1-fm
 * cbrssdr1-honors
 * cbrssdr1-meb
 * cbrssdr1-smt
 * cbrssdr1-ustar
 
While it can be difficult, this experiment and tutorial works best when you have access
to all **8** CBRS nodes listed above. In the future, I hope to make this experiment more 
flexible in its use of nodes and the number of nodes being used at one, but at this time, you
must have access to all 8 nodes. If that cannot happen, careful commenting out of certain
portions is possible, just difficult and annoying. t
The **reservation should also include** the same number of either d430 or d740 compute nodes 
(ideally this is 8). It can also be helpful to reserve the 3550 to 3560 frequency range. 

The collection of received signal strength data will use multi_power_tutorial.py,
multi_power_gather_tutorial.py, multi_combine_tutorial.py, and rx_tx_generic_tutorial.py Python
scripts. All of these should be downloaded in the same folder as they will be used together.

## Instantiate the Experiment ##

Using the CBRS rooftop nodes reserved above, instantiate an experiment on the POWDER platform
following these steps:

1. select **Experiments**
2. shoose **Start Experiment**
3. select **Change Profile**
4. find **signal_power**
5. click **Select Profile** then **Next**
6. choose the **Compute node type** you reserved (d740 or d430)
7. adjust **frequency range** to match the reservation
8. add the appropriate number of **X310 CBRS Radios** (ideally 8)
9. specify the **names** of the CBRS Radios you reserved
10. click **Next**

Now, your experiment will begin provisioning and botting up the resources you will be using.
This will take a few moments. You are ready to go once your screen shows **"Your experiment
is ready!"**

## Make the Changes ##

You now need to go into the Python code downloaded earlier and alter certain portions so that
everything will work for you and the resources allocated to you. This will require you know !! 
pieces of information:
1. the destination file name you would like to create (.csv)
2. location of ssh key_filename on your device
2. ssh password for your device
3. your POWDER username for ssh
4. ssh url for bes node
5. ssh url for browning node
6. ssh url for dentistry node
7. ssh url for fm node
8. ssh url for honors node
9. ssh url for meb node
10. ssh url for smt node
11. ssh url for ustar node



### multi_power_tutorial.py ###

 * **line 6:** Add destination file name you would like to create
  
### multi_power_gather_tutorial.py ###

  **no edits need to be made**
  
### rx_tx_generic_tutorial.py ###

  * **line 19:** Add password and browning ssh url
  * **line 24:** Add password and bes ssh url
  *  **line 29:** Add password and fm ssh url
  *  **line 34:** Add password and meb ssh url
  *  **line 39:** Add password and ustar ssh url  
  *  **line 44:** Add password and honors ssh url
  * **line 49:** Add password and smt ssh url
  * **line 54:** Add password and dentistry ssh url
  * **line 66:** Add browning url and username
  * **line 67:** Add key_filename location
  * **line 70:** Add bes url and username
  * **line 71:** Add key_filename location
  * **line 74:** Add meb url and username
  * **line 75:** Add key_filename location
  * **line 78:** Add ustar url and username
  * **line 79:** Add key_filename location
  * **line 82:** Add fm url and username
  * **line 83:** Add key_filename location
  * **line 86:** Add dentistry url and username
  * **line 87:** Add key_filename location
  * **line 90:** Add honors url and username
  * **line 91:** Add key_filename location
  * **line 94:** Add smt url and username
  * **line 95:** Add key_filename location
  
  ### multi_combine_tutorial.py ###
  
  **no edits need to be made**
  
  
## Running It ##
Now that all the necessary changes have been made, the script can be run and the received
signal strength data can be collected!

If everything was changed and inserted properly, the only thing that needs to be done now is 
run multi_power_tutorial.py. With that, you can watch as you transmit and receive from every
combination of transmitter and receiver. Due to the timing required for this, the entire 
process will take up to 14 minutes, but can run completely autonomous. 

## The Data ##
Once multi_power_tutorial.py is complete, a table of values can be found at whatever
destination file name you chose earlier. The csv file will be an 8-by-8 table of 
recieved signal strength values. The row corresponds to the transmitter while the
column corresponds to the reciever. 
