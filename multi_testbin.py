from fabric import Connection, Config
import time
from multiprocessing import Process
import subprocess


def fm_rx(connection):
    connection.run('uhd_rx_powerfile -f 3555e6 --lo-offset=1.2M -N 10000 fm_bin_power1')
    connection.run('bin_avg.py -p ~/fm_bin_power1 -w 5000 -n fm_bin_db_power')
    subprocess.call('pscp -pw kirby -scp alliet@pc14-fort.emulab.net:~/fm_bin_db_power.csv fm_bin_db_power.csv')
    return

def bes_rx(connection):
    connection.run('uhd_rx_powerfile -f 3555e6 --lo-offset=1.2M -N 10000 bes_bin_power')
    connection.run('bin_avg.py -p ~/bes_bin_power -w 5000 -n bes_bin_db_power')
    subprocess.call('pscp -pw kirby -scp alliet@pc06-fort.emulab.net:~/bes_bin_db_power.csv bes_bin_db_power.csv')
    return

def meb_rx(connection):
    connection.run('uhd_rx_powerfile -f 3555e6 --lo-offset=1.2M -N 10000 meb_bin_power')
    connection.run('bin_avg.py -p ~/meb_bin_power -w 5000 -n meb_bin_db_power')
    subprocess.call('pscp -pw kirby -scp alliet@pc14-fort.emulab.net:~/meb_bin_db_power.csv meb_bin_db_power.csv')
    return

def ustar_rx(connection):
    connection.run('uhd_rx_powerfile -f 3555e6 --lo-offset=1.2M -N 10000 ustar_bin_power')
    connection.run('bin_avg.py -p ~/ustar_bin_power -w 5000 -n ustar_bin_db_power')
    subprocess.call('pscp -pw kirby -scp alliet@pc15-fort.emulab.net:~/ustar_bin_db_power.csv ustar_bin_db_power.csv')
    return

def honors_rx(connection):
    connection.run('uhd_rx_powerfile -f 3555e6 --lo-offset=1.2M -N 10000 honors_bin_power')
    connection.run('bin_avg.py -p ~/honors_bin_power -w 5000 -n honors_bin_db_power')
    subprocess.call('pscp -pw kirby -scp alliet@pc09-fort.emulab.net:~/honors_bin_db_power.csv honors_bin_db_power.csv')
    return

def smt_rx(connection):
    connection.run('uhd_rx_powerfile -f 3555e6 --lo-offset=1.2M -N 10000 smt_bin_power')
    connection.run('bin_avg.py -p ~/smt_bin_power -w 5000 -n smt_bin_db_power')
    subprocess.call('pscp -pw kirby -scp alliet@pc10-fort.emulab.net:~/smt_bin_db_power.csv smt_bin_db_power.csv')
    return

def den_rx(connection):
    connection.run('uhd_rx_powerfile -f 3555e6 --lo-offset=1.2M -N 10000 den_bin_power')
    connection.run('bin_avg.py -p ~/den_bin_power -w 5000 -n den_bin_db_power')
    subprocess.call('pscp -pw kirby -scp alliet@pc06-fort.emulab.net:~/den_bin_db_power.csv den_bin_db_power.csv')
    return

def tx(connection):
    print('start transmit:')
    connection.run('uhd_siggen --const --freq 3555e6 --amplitude 1 --gain 31.5 -v')
    print('end transmit!')


if __name__ =='__main__':
    transmit_ssh = Connection(host='pc06-fort.emulab.net', user='alliet',
                    connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
#    fm_recieve_ssh = Connection(host='pc14-fort.emulab.net', user='alliet',
#                    connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
#    bes_recieve_ssh = Connection(host='pc06-fort.emulab.net', user='alliet',
#                connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    meb_recieve_ssh = Connection(host='pc14-fort.emulab.net', user='alliet',
                connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    ustar_recieve_ssh = Connection(host='pc15-fort.emulab.net', user='alliet',
                connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
#    honors_recieve_ssh = Connection(host='pc09-fort.emulab.net', user='alliet',
#                connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
#    smt_recieve_ssh = Connection(host='pc10-fort.emulab.net', user='alliet',
#                connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
#    den_recieve_ssh = Connection(host='pc06-fort.emulab.net', user='alliet',
#                connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})


    transmit = Process(target = tx, args = (transmit_ssh,))
    transmit.daemon = True

#    fm = Process(target = fm_rx, args = (fm_recieve_ssh,))
#    bes = Process(target = bes_rx, args = (bes_recieve_ssh,))
    meb = Process(target = meb_rx, args = (meb_recieve_ssh,))
    ustar = Process(target = ustar_rx, args = (ustar_recieve_ssh,))
#    honors = Process(target = honors_rx, args = (honors_recieve_ssh,))
#    smt = Process(target = smt_rx, args = (smt_recieve_ssh,))
#    den = Process(target = den_rx, args = (den_recieve_ssh,))

    transmit.start()
    time.sleep(30)
#    fm.start()
#    bes.start()
    meb.start()
    ustar.start()
#    honors.start()
#    smt.start()
#    den.start()

    transmit.join(1)
#    fm.join()
#    bes.join()
    meb.join()
    ustar.join()
#    honors.join()
#    smt.join()
#    den.join()
