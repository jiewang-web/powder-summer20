import rx_tx_generic
from fabric import Connection, Config

tx = Connection(host = 'pc750.emulab.net', user = 'alliet',
    connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})

rx_list = []
rx_names = []
rx1 = Connection(host = 'pc747.emulab.net', user = 'alliet',
    connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
rx_list.append(rx1)
rx_names.append('Browning')

rx2 = Connection(host = 'pc741.emulab.net', user = 'alliet',
    connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
rx_list.append(rx2)
rx_names.append('MEB')

rx3 = Connection(host = 'pc748.emulab.net', user = 'alliet',
    connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
rx_list.append(rx3)
rx_names.append('USTAR')

rx4 = Connection(host = 'pc742.emulab.net', user = 'alliet',
    connect_kwargs={'key_filename': '/Users/allis/Powder/paramiko/id_rsa'})
rx_list.append(rx4)
rx_names.append('Friendship Manor')

print(rx_names)

rx_tx_generic.run_it_all(tx, rx_list, rx_names)
