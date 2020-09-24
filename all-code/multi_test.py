from fabric import Connection, Config
import time
from multiprocessing import Process
import subprocess


def fm_rx(connection):
    connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 50000000 fm_power1')
    connection.run('iq_to_power.py -p ~/fm_power1 -w 25000000 -n fm_db_power')
    subprocess.call('pscp -pw kirby -scp alliet@pc788.emulab.net:~/fm_db_power.csv fm_db_power.csv')
    return

def bes_rx(connection):
    connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 50000000 bes_power')
    connection.run('iq_to_power.py -p ~/bes_power -w 25000000 -n bes_db_power')
    subprocess.call('pscp -pw kirby -scp alliet@pc784.emulab.net:~/bes_db_power.csv bes_db_power.csv')
    return

def meb_rx(connection):
    connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 50000000 meb_power')
    connection.run('iq_to_power.py -p ~/meb_power -w 25000000 -n meb_db_power')
    subprocess.call('pscp -pw kirby -scp alliet@pc785.emulab.net:~/meb_db_power.csv meb_db_power.csv')
    return

def ustar_rx(connection):
    connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 50000000 ustar_power')
    connection.run('iq_to_power.py -p ~/ustar_power -w 25000000 -n ustar_db_power')
    subprocess.call('pscp -pw kirby -scp alliet@pc790.emulab.net:~/ustar_db_power.csv ustar_db_power.csv')
    return

def honors_rx(connection):
    connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 50000000 honors_power')
    connection.run('iq_to_power.py -p ~/honors_power -w 25000000 -n honors_db_power')
    subprocess.call('pscp -pw kirby -scp alliet@pc794.emulab.net:~/honors_db_power.csv honors_db_power.csv')
    return

def smt_rx(connection):
    connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 50000000 smt_power')
    connection.run('iq_to_power.py -p ~/smt_power -w 25000000 -n smt_db_power')
    subprocess.call('pscp -pw kirby -scp alliet@pc791.emulab.net:~/smt_db_power.csv smt_db_power.csv')
    return

def den_rx(connection):
    connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 50000000 den_power')
    connection.run('iq_to_power.py -p ~/den_power -w 25000000 -n den_db_power')
    subprocess.call('pscp -pw kirby -scp alliet@pc793.emulab.net:~/den_db_power.csv den_db_power.csv')
    return

def brown_tx(connection):
    print('start transmit:')
    connection.run('uhd_siggen --const --freq 3555e6 --amplitude 1 --gain 31.5 -v')
    print('end transmit!')


if __name__ =='__main__':
    brown_transmit_ssh = Connection(host='pc786.emulab.net', user='alliet',
                    connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    fm_recieve_ssh = Connection(host='pc788.emulab.net', user='alliet',
                    connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    bes_recieve_ssh = Connection(host='pc784.emulab.net', user='alliet',
                connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    meb_recieve_ssh = Connection(host='pc785.emulab.net', user='alliet',
                connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    ustar_recieve_ssh = Connection(host='pc790.emulab.net', user='alliet',
                connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    honors_recieve_ssh = Connection(host='pc794.emulab.net', user='alliet',
                connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    smt_recieve_ssh = Connection(host='pc791.emulab.net', user='alliet',
                connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    den_recieve_ssh = Connection(host='pc793.emulab.net', user='alliet',
                connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})


    brown_transmit = Process(target = brown_tx, args = (brown_transmit_ssh,))
    brown_transmit.daemon = True

    fm = Process(target = fm_rx, args = (fm_recieve_ssh,))
    bes = Process(target = bes_rx, args = (bes_recieve_ssh,))
    meb = Process(target = meb_rx, args = (meb_recieve_ssh,))
    ustar = Process(target = ustar_rx, args = (ustar_recieve_ssh,))
    honors = Process(target = honors_rx, args = (honors_recieve_ssh,))
    smt = Process(target = smt_rx, args = (smt_recieve_ssh,))
    den = Process(target = den_rx, args = (den_recieve_ssh,))

    brown_transmit.start()

    fm.start()
    bes.start()
    meb.start()
    ustar.start()
    honors.start()
    smt.start()
    den.start()

    brown_transmit.join(1)
    fm.join()
    bes.join()
    meb.join()
    ustar.join()
    honors.join()
    smt.join()
    den.join()
