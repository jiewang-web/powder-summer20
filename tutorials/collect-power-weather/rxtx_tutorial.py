from fabric import Connection, Config
import time
import subprocess
from multiprocessing import Process

def recieve(connection):
    print('in recieve')
    connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 10000 test_bin_power1')
    connection.run('iq_to_power.py -p ~/test_bin_power1 -w 5000 -n bin_db_power1')
    subprocess.call('pscp -pw (add ssh password) -scp (add ssh node url + username):~/bin_db_power1.csv new_siggen_file1.csv')
    print('end recieve')
    return

def transmit(connection):
    print('start transmit:')
    connection.run('uhd_siggen_45sec --const --freq 3555e6 --amplitude 1 --gain 31.5 -v')
    print('end transmit!')

# Add correct SSH location for transmit node + location of SSH key_filename
transmit_ssh = Connection(host='add node ssh url', user='add username',
                connect_kwargs={'key_filename': 'location of ssh key_filename'})

# Add correct SSH location for receive node + location of SSH key_filename
recieve_ssh = Connection(host='add node ssh url', user='add username',
                connect_kwargs={'key_filename': 'location of ssh key_filename'})

if __name__ == '__main__':
    p1 = Process(target = transmit, args = (transmit_ssh,))

    p2 = Process(target = recieve, args = (recieve_ssh,))

    p1.start()
    time.sleep(30)
    print('start recieve process')
    p2.start()
