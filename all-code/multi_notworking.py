from fabric import Connection, Config
from multiprocessing import Process
import subprocess
import sys

def gather_ssh():
    num_brown = input('Browning SSH Number? (if not press enter)')
    num_fm = input('Friendship Manor SSH Number? (if not press enter)')
    num_bes = input('Behavioral SSH Number? (if not press enter)')
    num_meb = input('MEB SSH Number? (if not press enter)')
    num_ustar = input('USTAR SSH Number? (if not press enter')
    num_honors = input('Honors SSH Number? (if not press enter)')
    num_smt = input('Medical SSH Number? (if not press enter)')
    num_den = input('Dentistry SSH Number? (if not press enter)')

    return num_brown, num_fm, num_bes, num_meb, num_ustar, num_honors, num_smt, num_den

def nums_and_names(num_brown, num_fm, num_bes, num_meb, num_ustar, num_honors, num_smt, num_den):
    node_nums = []
    node_names = []
#    node_nums_and_names = []

    if num_brown != '':
        node_nums.append(num_brown)
        node_names.append('Browning')
#        node_nums_and_names.append([num_brown, 'Browning'])

    if num_fm != '':
        node_nums.append(num_fm)
        node_names.append('Friendship Manor')
#        node_nums_and_names.append([num_fm, 'Friendship Manor'])

    if num_bes != '':
        node_nums.append(num_bes)
        node_names.append('Behavioral')
#        node_nums_and_names.append([num_bes, 'Behavioral'])

    if num_meb != '':
        node_nums.append(num_meb)
        node_names.append('MEB')
#        node_nums_and_names.append([num_meb, 'MEB'])

    if num_ustar != '':
        node_nums.append(num_ustar)
        node_names.append('USTAR')
#        node_nums_and_names.append([num_ustar, 'USTAR'])

    if num_honors != '':
        node_nums.append(num_honors)
        node_names.append('Honors')
#        node_nums_and_names.append([num_honors, 'Honors'])

    if num_smt != '':
        node_nums.append(num_smt)
        node_names.append('Medical')
#        node_nums_and_names.append([num_smt, 'Medical'])

    if num_den != '':
        node_nums.append(num_den)
        node_names.append('Dentistry')
#        node_nums_and_names.append([num_den, 'Dentistry'])

#    return node_nums_and_names
    return node_nums, node_names

def ssh_in(i, node_num, node_names):
    hostname = 'pc' + i + '.emulab.net'
    index = node_num.index(i)
    name = node_names[index]

    if name == 'Browning':
        print('Browning Connection')
        ssh_brown = Connection(host = hostname, user = 'alliet',
            connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
        return ssh_brown

    elif name == 'Friendship Manor':
        print('Friendship Manor Connection')
        ssh_fm = Connection(host = hostname, user = 'alliet',
            connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
        return ssh_fm

    elif name == 'Behavioral':
        print('Behavioral Connection')
        ssh_bes = Connection(host = hostname, user = 'alliet',
            connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
        return ssh_bes

    elif name == 'MEB':
        print('MEB Connection')
        ssh_meb = Connection(host = hostname, user = 'alliet',
            connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
        return ssh_meb

    elif name == 'USTAR':
        print('USTAR Connection')
        ssh_ustar = Connection(host = hostname, user = 'alliet',
            connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
        return ssh_ustar

    elif name == 'Honors':
        print('Honors Connection')
        ssh_honors = Connection(host = hostname, user = 'alliet',
            connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
        return ssh_honors

    elif name == 'Medical':
        print('Medical Connection')
        ssh_smt = Connection(host = hostname, user = 'alliet',
            connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
        return ssh_smt

    elif name == 'Dentistry':
        print('Dentistry Connection')
        ssh_den = Connection(host = hostname, user = 'alliet',
            connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
        return ssh_den

def ssh_all(node_num, node_names):
    ssh_connections = []
    for i in node_num:
        ssh_connect = ssh_in(i, node_num, node_names)
        ssh_connections.append(ssh_connect)
    return ssh_connections

def tx(connection):
    print('start transmit:')
    connection.run('uhd_siggen --const --freq 3555e6 --amplitude 1 --gain 31.5')
    print('end transmit!')

def rx(connection, rx_names):
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

def write_current_to_file(tx_name):
    power_row = []
    for a in node_names:
        if a == 'Browning':
            if a == tx_name:
                power_row.append('-')
            else:
                with open('brown_db_power.csv', newline='') as file:
                    brown_power = csv.reader(file, quoting = csv.QUOTE_NONNUMERIC)
                    for row in brown_power:
                        brown_current_power = row
                power_row.append(brown_current_power[0])

        elif a == 'Friendship Manor':
            if a == tx_name:
                power_row.append('-')
            else:
                with open('fm_db_power.csv', newline='') as file:
                    fm_power = csv.reader(file, quoting = csv.QUOTE_NONNUMERIC)
                    for row in fm_power:
                        fm_current_power = row
                power_row.append(fm_current_power[0])

        elif a == 'Behavioral':
            if a == tx_name:
                power_row.append('-')
            else:
                with open('bes_db_power.csv', newline='') as file:
                    bes_power = csv.reader(file, quoting = csv.QUOTE_NONNUMERIC)
                    for row in bes_power:
                        bes_current_power = row
                power_row.append(bes_current_power[0])

        elif a == 'MEB':
            if a == tx_name:
                power_row.append('-')
            else:
                with open('meb_db_power.csv', newline='') as file:
                    meb_power = csv.reader(file, quoting = csv.QUOTE_NONNUMERIC)
                    for row in meb_power:
                        meb_current_power = row
                power_row.append(meb_current_power[0])

        elif a == 'USTAR':
            if a == tx_name:
                power_row.append('-')
            else:
                with open('ustar_db_power.csv', newline='') as file:
                    ustar_power = csv.reader(file, quoting = csv.QUOTE_NONNUMERIC)
                    for row in ustar_power:
                        ustar_current_power = row
                power_row.append(ustar_current_power[0])

        elif a == 'Honors':
            if a == tx_name:
                power_row.append('-')
            else:
                with open('honors_db_power.csv', newline='') as file:
                    honors_power = csv.reader(file, quoting = csv.QUOTE_NONNUMERIC)
                    for row in honors_power:
                        honors_current_power = row
                power_row.append(honors_current_power[0])

        elif a == 'Medical':
            if a == tx_name:
                power_row.append('-')
            else:
                with open('smt_db_power.csv', newline='') as file:
                    smt_power = csv.reader(file, quoting = csv.QUOTE_NONNUMERIC)
                    for row in smt_power:
                        smt_current_power = row
                power_row.append(smt_current_power[0])

        elif a == 'Dentistry':
            if a == tx_name:
                power_row.append('-')
            else:
                with open('den_db_power.csv', newline='') as file:
                    den_power = csv.reader(file, quoting = csv.QUOTE_NONNUMERIC)
                    for row in den_power:
                        den_current_power = row
                power_row.append(den_current_power[0])

    with open('multi_power_file.csv', 'w', newline='') as power_file:
        power_writer = csv.writer(power_file, delimiter=',', wuoting=csv.QUOTE_MINIMAL)
        power_writer.writerow(power_row)

def combining_it():
    num_brown, num_fm, num_bes, num_meb, num_ustar, num_honors, num_smt, num_den = gather_ssh()
    print('collected ssh numbers')
    node_num, node_names = nums_and_names(num_brown, num_fm, num_bes, num_meb, num_ustar, num_honors, num_smt, num_den)
    print('collected number and name combos')
    #node_nums_and_names = nums_and_names()
    ssh_connections = ssh_all(node_num, node_names)
    print('made ssh connections')
    return ssh_connections, node_num, node_names

def transmit():
    for j in node_num:
        rx_connections = []
        rx_names = []
        rx_all = []
        tx_index = node_num.index(j)
        tx_name = node_names[tx_index]
        tx_connection = ssh_connections[tx_index]
        print('set variables complete in tx')
        for k in node_names:
            if k != tx_name








for j in node_num:
    rx_connections = []
    rx_names = []
    rx_all = []
    tx_index = node_num.index(j)
    tx_name = node_names[tx_index]
    tx_connection = ssh_connections[tx_index]
    print('set variables complete')
    for k in node_names:
        if k != tx_name:
            rx_index = node_names.index(k)
            rx_connection = ssh_connections[rx_index]
            rx_connections.append(rx_connection)
            rx_names.append(k)
    print('reciever variables set')
    print(__name__)
    if __name__ == '__main__':
        print('in if statement')
        tx_p = Process(target = tx, args = (tx_connection,))
        tx_p.daemon = True
        print('tx process created')
        for m in rx_connections:
            rx_1 = Process(target = rx, args= (m,rx_names,))
            rx_all.append(rx_1)
        print('rx processes created')
        tx_p.start()
        print('tx process started')
        for n in rx_all:
            n.start()
            print('in rx process starting')
        print('rx processes started')
        tx_p.join(1)

        for p in rx_all:
            p.join()
#    write_current_to_file(tx_name)
print('this is the end <3')
sys.exit()
#print('why isnt this ending!!!')
