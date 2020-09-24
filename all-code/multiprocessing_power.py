from multiprocessing import Process

def recieve(connection, rx_name):
    connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 50000000 power1')
    connection.run('iq_to_power.py -p ~/power1 -w 25000000 -n db_power1')
    subprocess.call('pscp -pw kirby -scp alliet@pc784.emulab.net:~/db_power1.csv db_power4.csv')
    return

print('start recieve:')

connect_index = rx_connections.index(connection)
for q in rx_names:
    name_index = rx_names.index(q)
    if name_index == connect_index and q == 'Browning':
        connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 50000000 brown_power')
        connection.run('iq_to_power.py -p ~/brown_power -w 25000000 -n brown_db_power')
        subprocess.call('pscp -pw kirby -scp alliet@pc793.emulab.net:~/brown_db_power.csv brown_db_power.csv')
        print('end browning recieve!')

    if name_index == connect_index and q == 'Friendship Manor':
        connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 50000000 fm_power')
        connection.run('iq_to_power.py -p ~/fm_power -w 25000000 -n fm_db_power')
        subprocess.call('pscp -pw kirby -scp alliet@pc793.emulab.net:~/fm_db_power.csv fm_db_power.csv')
        print('end friendship manor recieve!')

    if name_index == connect_index and q == 'Behavioral':
        connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 50000000 bes_power')
        connection.run('iq_to_power.py -p ~/bes_power -w 25000000 -n bes_db_power')
        subprocess.call('pscp -pw kirby -scp alliet@pc793.emulab.net:~/bes_db_power.csv bes_db_power.csv')
        print('end Behavioral recieve!')

    if name_index == connect_index and q == 'MEB':
        connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 50000000 meb_power')
        connection.run('iq_to_power.py -p ~/meb_power -w 25000000 -n meb_db_power')
        subprocess.call('pscp -pw kirby -scp alliet@pc793.emulab.net:~/meb_db_power.csv meb_db_power.csv')
        print('end browning recieve!')

    if name_index == connect_index and q == 'USTAR':
        connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 50000000 ustar_power')
        connection.run('iq_to_power.py -p ~/ustar_power -w 25000000 -n ustar_db_power')
        subprocess.call('pscp -pw kirby -scp alliet@pc793.emulab.net:~/ustar_db_power.csv ustar_db_power.csv')
        print('end ustar recieve!')

    if name_index == connect_index and q == 'Honors':
        connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 50000000 honors_power')
        connection.run('iq_to_power.py -p ~/honors_power -w 25000000 -n honors_db_power')
        subprocess.call('pscp -pw kirby -scp alliet@pc793.emulab.net:~/honors_db_power.csv honors_db_power.csv')
        print('end honors recieve!')

    if name_index == connect_index and q == 'Medical':
        connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 50000000 smt_power')
        connection.run('iq_to_power.py -p ~/smt_power -w 25000000 -n smt_db_power')
        subprocess.call('pscp -pw kirby -scp alliet@pc793.emulab.net:~/smt_db_power.csv smt_db_power.csv')
        print('end medical recieve!')

    if name_index == connect_index and q == 'Dentistry':
        connection.run('uhd_rx_cfile -f 3555e6 --lo-offset=1.2M -N 50000000 den_power')
        connection.run('iq_to_power.py -p ~/den_power -w 25000000 -n den_db_power')
        subprocess.call('pscp -pw kirby -scp alliet@pc793.emulab.net:~/den_db_power.csv den_db_power.csv')
        print('end Dentistry recieve!')

return
def transmit(connection):
    print('start transmit:')
    connection.run('uhd_siggen --const --freq 3555e6 --amplitude 1 --gain 31.5 -v')
    print('end transmit!')


def everything(tx_connection, rx_connection, rx_name):
    if __name__ == '__main__':
        tx_p = Process(target = transmit, args = (tx_connection,))
        tx_p.daemon = True

        rx_p = Process(target = recieve, args = (rx_connection, rx_name,))

        tx_p.start()
        rx_p.start()
        tx_p.join(1)
        rx_p.join()




everything()
