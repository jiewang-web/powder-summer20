import csv
import pandas

def writetofile(file_name, tx_name):

    fm_power = ['Friendship Manor']
    ustar_power = ['USTAR']
    smt_power = ['Medical']
    den_power = ['Dentistry']
    brown_power = ['Browning']

    if tx_name == 'FriendshipManor':
        fm_current_power = '-------------'
        fm_power.append(fm_current_power)
    else:
        with open('fm_bin_db_power.csv', newline='') as fm_csvFile:
            fm_powerreader = csv.reader(fm_csvFile, quoting=csv.QUOTE_NONNUMERIC)
            for row in fm_powerreader:
                fm_current_power = row
            i = len(fm_current_power)
            index = i - 1
            fm_power.append(fm_current_power[index])

    if tx_name == 'USTAR':
        ustar_current_power = '-------------'
        ustar_power.append(ustar_current_power)
    else:
        with open('ustar_bin_db_power.csv', newline='') as ustar_csvFile:
            ustar_powerreader = csv.reader(ustar_csvFile, quoting=csv.QUOTE_NONNUMERIC)
            for row in ustar_powerreader:
                ustar_current_power = row
        i = len(ustar_current_power)
        index = i - 1
        ustar_power.append(ustar_current_power[index])

    if tx_name == 'Medical':
        smt_current_power = '-------------'
        smt_power.append(smt_current_power)
    else:
        with open('smt_bin_db_power.csv', newline='') as smt_csvFile:
            smt_powerreader = csv.reader(smt_csvFile, quoting=csv.QUOTE_NONNUMERIC)
            for row in smt_powerreader:
                smt_current_power = row
        i = len(smt_current_power)
        index = i - 1
        smt_power.append(smt_current_power[index])

    if tx_name == 'Dentistry':
        den_current_power = '-------------'
        den_power.append(den_current_power)
    else:
        with open('den_bin_db_power.csv', newline='') as den_csvFile:
            den_powerreader = csv.reader(den_csvFile, quoting=csv.QUOTE_NONNUMERIC)
            for row in den_powerreader:
                den_current_power = row
        i = len(den_current_power)
        index = i - 1
        den_power.append(den_current_power[index])

    if tx_name == 'Browning':
        brown_current_power = '-------------'
        brown_power.append(brown_current_power)
    else:
        with open('brown_bin_db_power.csv', newline='') as brown_csvFile:
            brown_powerreader = csv.reader(brown_csvFile, quoting=csv.QUOTE_NONNUMERIC)
            for row in brown_powerreader:
                brown_current_power = row
        i = len(brown_current_power)
        index = i - 1
        brown_power.append(brown_current_power[index])

    with open(file_name, 'w', newline='') as power_file:
        power_writer = csv.writer(power_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        power_writer.writerow(brown_power)
        power_writer.writerow(den_power)
        power_writer.writerow(fm_power)
        
        power_writer.writerow(smt_power)
        power_writer.writerow(ustar_power)

#tx_index = 9

def gettx(index):
    tx_index=[index]
    with open('tx_index.csv', 'w', newline='') as index_file:
        index_writer = csv.writer(index_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        index_writer.writerow(tx_index)

def returntx():
    index = pandas.read_csv('tx_index.csv', header=None)
    print(index[0][0])
    return index[0][0]
