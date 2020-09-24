import pandas
import csv

def combine_files(com_filename):
    fm = pandas.read_csv('FriendshipManor_tx_pw_file.csv', header = None)

    ustar = pandas.read_csv('USTAR_tx_pw_file.csv', header = None)

    smt = pandas.read_csv('Medical_tx_pw_file.csv', header = None)
    den = pandas.read_csv('Dentistry_tx_pw_file.csv', header = None)
    brown = pandas.read_csv('Browning_tx_pw_file.csv', header = None)

    labels = fm[0]
    top_row = ['',labels[0], labels[1], labels[2], labels[3], labels[4]]
    fm_num = fm[1]

    ustar_num = ustar[1]

    smt_num = smt[1]
    den_num = den[1]
    brown_num = brown[1]

    #print (fm_num[0])
    fm_row = [labels[2]]

    ustar_row = [labels[4]]

    smt_row = [labels[3]]
    den_row = [labels[1]]
    brown_row = [labels[0]]

    #print(fm_row)
    index = 0
    while index <= 4:
        fm_row.append(fm_num[index])

        ustar_row.append(ustar_num[index])

        smt_row.append(smt_num[index])
        den_row.append(den_num[index])
        brown_row.append(brown_num[index])
        index = index + 1


    with open(com_filename, 'w', newline='') as power_file:
        power_writer = csv.writer(power_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        power_writer.writerow(top_row)

        power_writer.writerow(brown_row)
        power_writer.writerow(den_row)
        power_writer.writerow(fm_row)

        power_writer.writerow(smt_row)
        power_writer.writerow(ustar_row)
