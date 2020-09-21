import subprocess
import multi_power_gather
import multi_combine
import time

filename = 'pw_table10_edit.csv'

#i=0

#while i <= 4 :
#    multi_power_gather.gettx(i)
#    subprocess.run('python rx_tx_generic_edit.py')
#    i = i + 1

print('Finished all Transmission and Reception')
multi_combine.combine_files(filename)
