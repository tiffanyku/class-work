"""
7.2 prompt for file name

read lines of file

count = 0

num = 0

look for X-DSPAM-Confidence:0.8475

    if it has X-DSPAM

        count + 1

        traverse to colon

        split = convert to float

        num + split 

average = num / count

print average

"""
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print ('File cannot be opened: ', fname)
    exit()
    
count = 0
num = 0.0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        nline = float(line[20:])
        num += nline
        count += 1
avg = num / count
print('Average spam confidence: ', avg)

fhand.close()