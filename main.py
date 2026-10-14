fin = open('mailbox.txt', 'r')
lines = fin.readlines()

fout = open('output.txt', 'w')

counter = 0
found = False

for line in lines:
    if line.startswith('Log:'):
        found = True
        continue

    if found:
        if line.startswith('----------------------'):
            found = False
            fout.write('\n')
        else:
            print(line, end='')




