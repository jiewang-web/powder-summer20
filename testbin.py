from fabric import Connection, Config
import time
from multiprocessing import Process
import subprocess
import time

def timing(connection):
#    time.sleep(5)
    connection.run('uhd_rx_powerfile -f 3555e6 --lo-offset=1.2M -N 10000 test_bin_power1')
    connection.run('bin_avg.py -p ~/test_bin_power1 -w 5000 -n bin_db_power1')
    subprocess.call('pscp -pw kirby -scp alliet@pc02-meb.emulab.net:~/bin_db_power1.csv single_test_bin_db_power3.csv')
    return

def transmit(connection):
    print('start transmit:')
    connection.run('uhd_siggen --const --freq 3555e6 --amplitude 1 --gain 31.5 -v')
    print('end transmit!')

if __name__ =='__main__':
    transmit_ssh = Connection(host='pc12-fort.emulab.net', user='alliet',
                    connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    recieve_ssh = Connection(host='pc02-meb.emulab.net', user='alliet',
                    connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    p1 = Process(target = transmit, args = (transmit_ssh,))
    p1.daemon = True

    p2 = Process(target = timing, args = (recieve_ssh,))

    p1.start()
    time.sleep(30)
    p2.start()

    p1.join(1)
    p2.join()
