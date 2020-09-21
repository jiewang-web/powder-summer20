from fabric import Connection, Config
import time
from multiprocessing import Process
import subprocess

def timing(connection):
    connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 10000 power1')
    connection.run('iq_to_power.py -p ~/power1 -w 5000 -n db_power1')
    subprocess.call('pscp -pw kirby -scp alliet@pc817.emulab.net:~/db_power1.csv ustar_test1.csv')
    return

def transmit(connection):
    print('start transmit:')
    connection.run('uhd_siggen_45sec --const --freq 3555e6 --amplitude 1 --gain 31.5 -v')
    print('end transmit!')


if __name__ =='__main__':
    transmit_ssh = Connection(host='pc785.emulab.net', user='alliet',
                    connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    recieve_ssh = Connection(host='pc817.emulab.net', user='alliet',
                    connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    p1 = Process(target = transmit, args = (transmit_ssh,))

    p2 = Process(target = timing, args = (recieve_ssh,))

    p1.start()
    time.sleep(30)
    p2.start()
