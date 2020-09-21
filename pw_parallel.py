from fabric import Connection, Config
from invoke import Responder
#import getpass
import subprocess
import matplotlib.pyplot as plt
#import pandas
#import numpy
from multiprocessing import Process
#import sys


ssh_transmit = Connection(host='pc12-fort.emulab.net', user='alliet',
                        connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
ssh_recieve = Connection(host='pc09-fort.emulab.net', user='alliet',
                        connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
#endRecieve = False

def transmit_connection_check():
    try:
        ssh_transmit.run('ls', timeout=5)
        print('True')
    except Exception as e:
        print('Connection lost: %s' %e)
        print('False')

def recieve_connection_check():
    try:
        ssh_transmit.run('ls', timeout=5)
        print('True')
    except Exception as e:
        print('Connection lost: %s' %e)
        print('False')

def transmit():
    print('start transmit:')
    #ssh_transmit.run(' ')
    ssh_transmit.close()
    ssh_transmit = Connection(host='pc12-fort.emulab.net', user='alliet',
                            connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    ssh_transmit.run('uhd_siggen --const --freq 3555e6 --amplitude 1 --gain 31.5 -v')
    print('end transmit!')

def end_transmit():
    print('start end transmit:')
    while True:
        if endRecieve == True:
            ssh_transmit.close()

def recieve():
    print('start recieve:')
    ssh_recieve.close()
    ssh_recieve = Connection(host='pc09-fort.emulab.net', user='alliet',
                            connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    ssh_recieve.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 50000000 power1')
    ssh_recieve.run('iq_to_power.py -p ~/power1 -w 25000000 -n db_power1' )
    subprocess.call('pscp -pw kirby -scp alliet@pc09-fort.emulab.net:~/db_power1.csv db_power1.csv')
    #ssh_transmit.run('^C')
#    endRecieve = True
#    print(endRecieve)
    print('end recieve!')


if __name__ == '__main__':
    #transmit_connection_check()
    #recieve_connection_check()
    p1 = Process(target = transmit)
    p1.start()
    p2 = Process(target = recieve)
    p2.start()
    #p3 = Process(target = end_transmit)
    #p3.start()
#    if endRecieve == True:
#        ssh_transmit.run(' ')
#        endRecieve = False
