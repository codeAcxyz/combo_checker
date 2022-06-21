import random

nf_acc = open('combo.txt', 'w+')


for x in range(10000000):
    result_str = ''.join((random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(20)))
    result_str = result_str[0:5] + "-" + result_str[5:10] + "-" + result_str[10:15] + "-" + result_str[15:20]
    print(x)
    nf_acc.write(result_str)
    nf_acc.write("\n")
nf_acc.close()
