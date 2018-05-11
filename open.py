#7.1

#ask for user input
#open file

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print ('File cannot be opened: ', fname)
    exit()
for line in fhand:
    print(line.upper())

fname.close()