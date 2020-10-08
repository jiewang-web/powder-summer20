import time
from multiprocessing import Process
from fabric import Connection, Config
import subprocess
import multi_power_gather

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
            subprocess.call('pscp -pw ADD PASSWORD -scp ADD BROWNING URL:~/brown_bin_db_power.csv brown_bin_db_power.csv')

        elif rx_names_list[connect_index] == 'Behavioral':
            connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 10000 bes_bin_power')
            connection.run('iq_to_power.py -p ~/bes_bin_power -w 5000 -n bes_bin_db_power')
            subprocess.call('pscp -pw ASS PASSWORD -scp ADD BES URL:~/bes_bin_db_power.csv bes_bin_db_power.csv')

        elif rx_names_list[connect_index] == 'FriendshipManor':
            connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 10000 fm_bin_power')
            connection.run('iq_to_power.py -p ~/fm_bin_power -w 5000 -n fm_bin_db_power')
            subprocess.call('pscp -pw ADD PASSWORD -scp ADD FM URL:~/fm_bin_db_power.csv fm_bin_db_power.csv')

        elif rx_names_list[connect_index] == 'MEB':
            connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 10000 meb_bin_power')
            connection.run('iq_to_power.py -p ~/meb_bin_power -w 5000 -n meb_bin_db_power')
            subprocess.call('pscp -pw ADD PASSWORD -scp ADD MEB URL:~/meb_bin_db_power.csv meb_bin_db_power.csv')

        elif rx_names_list[connect_index] == 'USTAR':
            connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 10000 ustar_bin_power')
            connection.run('iq_to_power.py -p ~/ustar_bin_power -w 5000 -n ustar_bin_db_power')
            subprocess.call('pscp -pw ADD PASSWORD -scp ADD USTAR URL:~/ustar_bin_db_power.csv ustar_bin_db_power.csv')

        elif rx_names_list[connect_index] == 'Honors':
            connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 10000 honors_bin_power')
            connection.run('iq_to_power.py -p ~/honors_bin_power -w 5000 -n honors_bin_db_power')
            subprocess.call('pscp -pw ADD PASSWORD -scp ADD HONORS URL:~/honors_bin_db_power.csv honors_bin_db_power.csv')

        elif rx_names_list[connect_index] == 'Medical':
            connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 10000 smt_bin_power')
            connection.run('iq_to_power.py -p ~/smt_bin_power -w 5000 -n smt_bin_db_power')
            subprocess.call('pscp -pw ADD PASSWORD -scp ADD SMT URL:~/smt_bin_db_power.csv smt_bin_db_power.csv')

        elif rx_names_list[connect_index] == 'Dentistry':
            connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 10000 den_bin_power')
            connection.run('iq_to_power.py -p ~/den_bin_power -w 5000 -n den_bin_db_power')
            subprocess.call('pscp -pw ADD PASSWORD -scp ADD DENTISTRY URL:~/den_bin_db_power.csv den_bin_db_power.csv')


    print('end reception')
    filename = tx_name + '_tx_pw_file.csv'
    multi_power_gather.writetofile(filename, tx_name)

def rx_tx_decision():

    all_names = ['Browning', 'Behavioral', 'MEB', 'USTAR', 'FriendshipManor', 'Dentistry', 'Honors', 'Medical']
    all_connections = []

    brown = Connection(host = 'ADD BROWNING URL', user = 'ADD USERNAME',
        connect_kwargs={'key_filename': 'ADD KEY_FILENAME LOCATION'})
    all_connections.append(brown)

    bes = Connection(host = 'ADD BES URL', user = 'ADD USERNAME',
        connect_kwargs={'key_filename': 'ADD KEY_FILENAME LOCATION'})
    all_connections.append(bes)

    meb = Connection(host = 'ADD MEB URL', user = 'ADD USERNAME',
        connect_kwargs={'key_filename': 'ADD KEY_FILENAME LOCATION'})
    all_connections.append(meb)

    ustar = Connection(host = 'ADD USTAR URL', user = 'ADD USERNAME',
        connect_kwargs={'key_filename': 'ADD KEY_FILENAME LOCATION'})
    all_connections.append(ustar)

    fm = Connection(host = 'ADD FM URL', user = 'ADD USERNAME',
        connect_kwargs={'key_filename': 'ADD KEY_FILENAME LOCATION'})
    all_connections.append(fm)

    den = Connection(host = 'ADD DENTISTRY URL', user = 'ADD USERNAME',
        connect_kwargs={'key_filename': 'ADD KEY_FILENAME LOCATION'})
    all_connections.append(den)

    honors = Connection(host = 'ADD HONORS URL', user = 'ADD USERNAME',
        connect_kwargs={'key_filename': 'ADD KEY_FILENAME LOCATION'})
    all_connections.append(honors)

    smt = Connection(host = 'ADD SMT URL', user = 'ADD USERNAME',
        connect_kwargs={'key_filename': 'ADD KEY_FILENAME LOCATION'})
    all_connections.append(smt)

    rx_list = []
    rx_names = []

    tx_i_str = multi_power_gather.returntx()
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
