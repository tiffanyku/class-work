#6.1 
#traverse through a string using while loop
#start at end of string and print letter on each line
fruit = 'banana'
index = len(fruit) - 1
while index >=0:
    letter = fruit[index]
    print (letter)
    index = index - 1

#6.2
#[:] shows the entire string
fruit = 'banana'
fruit [:]
fruit [3:]

#6.3
#function that takes a word and a letter as inputs
#check to make sure inputs are strings
#for loop that matches input letter to letters in the word
#print # of times the letter appears
def count (word, letter):
    word = str(word)
    letter = str(letter)
    count = 0
    for ls in word:
        if ls == letter : count += 1
    print (count)
#output
count (8888888, 8)
7

#6.4
#count number of times the letter a appears in string banana
fruit = "banana"
print(fruit.count("a"))

#output
3

#6.5
#take string and traverse to part of string after colon
#convert rest of string to float
#print the float 
str = 'X-DSPAM-Confidence: 0.8475'
start = str.find(":")
num = float(str[start+1:])
print(num)

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

#output
Enter the file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008

RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>

RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])

     BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;

     SAT, 05 JAN 2008 09:14:16 -050

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

#output
Enter the file name: mbox-short.txt
Average spam confidence:  0.7507185185185187 

#7.3
fname = input('Enter the file name: ')
count = 0
try:
    fhand = open(fname)
except:
    if fname.upper() == "NA NA BOO BOO":
        print("NA NA BOO BOO TO YOU - You've been punked!")
    else:
        print("File cannot be opened: ", fname)
    quit()    
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print("There were {0} subject lines in {1}.".format(str(count), fname))
fhand.close()