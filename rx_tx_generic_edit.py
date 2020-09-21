import time
from multiprocessing import Process
from fabric import Connection, Config
import subprocess
import multi_power_gather_edit

def not_tx(tx):
    print('start transmit')
    tx.run('uhd_siggen_90sec --const --freq 3555e6 --amplitude 1 --gain 31.5')
    print('end transmit')

def rx(tx_name, rx_connection_list, rx_names_list):
    print('start reception')
    for connection in rx_connection_list:
        connect_index = rx_connection_list.index(connection)
        if rx_names_list[connect_index] == 'Browning':
            connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 10000 brown_bin_power1')
            connection.run('iq_to_power.py -p ~/brown_bin_power1 -w 5000 -n brown_bin_db_power')
            subprocess.call('pscp -pw kirby -scp alliet@pc744.emulab.net:~/brown_bin_db_power.csv brown_bin_db_power.csv')


        elif rx_names_list[connect_index] == 'FriendshipManor':
            connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 10000 fm_bin_power')
            connection.run('iq_to_power.py -p ~/fm_bin_power -w 5000 -n fm_bin_db_power')
            subprocess.call('pscp -pw kirby -scp alliet@pc752.emulab.net:~/fm_bin_db_power.csv fm_bin_db_power.csv')


        elif rx_names_list[connect_index] == 'USTAR':
            connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 10000 ustar_bin_power')
            connection.run('iq_to_power.py -p ~/ustar_bin_power -w 5000 -n ustar_bin_db_power')
            subprocess.call('pscp -pw kirby -scp alliet@pc12-fort.emulab.net:~/ustar_bin_db_power.csv ustar_bin_db_power.csv')


        elif rx_names_list[connect_index] == 'Medical':
            connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 10000 smt_bin_power')
            connection.run('iq_to_power.py -p ~/smt_bin_power -w 5000 -n smt_bin_db_power')
            subprocess.call('pscp -pw kirby -scp alliet@pc745.emulab.net:~/smt_bin_db_power.csv smt_bin_db_power.csv')

        elif rx_names_list[connect_index] == 'Dentistry':
            connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 10000 den_bin_power')
            connection.run('iq_to_power.py -p ~/den_bin_power -w 5000 -n den_bin_db_power')
            subprocess.call('pscp -pw kirby -scp alliet@pc753.emulab.net:~/den_bin_db_power.csv den_bin_db_power.csv')


    print('end reception')
    filename = tx_name + '_tx_pw_file.csv'
    multi_power_gather_edit.writetofile(filename, tx_name)

def rx_tx_decision():

    all_names = ['Browning', 'USTAR', 'FriendshipManor', 'Dentistry',  'Medical']
    all_connections = []

    brown = Connection(host = 'pc744.emulab.net', user = 'alliet',
        connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    all_connections.append(brown)


    ustar = Connection(host = 'pc12-fort.emulab.net', user = 'alliet',
        connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    all_connections.append(ustar)

    fm = Connection(host = 'pc752.emulab.net', user = 'alliet',
        connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    all_connections.append(fm)

    den = Connection(host = 'pc753.emulab.net', user = 'alliet',
        connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    all_connections.append(den)


    smt = Connection(host = 'pc745.emulab.net', user = 'alliet',
        connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
    all_connections.append(smt)

    rx_list = []
    rx_names = []

    tx_i_str = multi_power_gather_edit.returntx()
    tx_i = int(tx_i_str)
#    tx_i = multi_power_gather.gettx(9)
    for name in all_names:
        i = all_names.index(name)
        if i == tx_i:
            tx = all_connections[tx_i]
            tx_name = all_names[tx_i]
        elif i != tx_i:
            rx_list.append(all_connections[i])
            rx_names.append(all_names[i])
#    print(rx_names)
    return tx, tx_name, rx_list, rx_names





if __name__ == '__main__':
    tx, tx_name, rx_list, rx_names = rx_tx_decision()
    print('tx:')
    print(tx)
    print('tx name:')
    print(tx_name)
    print('rx:')
    print(rx_list)
    print('rx names:')
    print(rx_names)

    p1 = Process(target = not_tx, args = (tx,))
#    p1.daemon = True
    rx_process = Process(target = rx, args = (tx_name, rx_list, rx_names,))
    print('processes created')
    p1.start()
    time.sleep(30)
    rx_process.start()
#    p1.join(1)
#    rx_process.join()
