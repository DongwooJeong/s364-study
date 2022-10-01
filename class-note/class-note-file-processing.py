xfile = open("mbox-short.txt")
count=0
for x in xfile:
    count+=1
print(count)

xfile=open("mbox-short.txt",'r')
inp=xfile.read()
print(len(inp))

xfile=open("mbox-short.txt",'r')
for line in xfile:
    line = line.rstrip()
    if line.startswith('From: '):
        print(line)

xfile=open("mbox-short.txt",'r')
for line in xfile:
    line = line.rstrip()
    if '@uct.ac.za' in line:
        print(line)

fhand=open("mbox-short.txt",'r')

fname = input('Enter the file name:  ')
try:
      fhand = open(fname)
except:
      print('File cannot be opened:', fname)
      quit()

count = 0
for line in fhand:
      if line.startswith('Subject:') :
          count = count + 1
print('There were', count, 'subject lines in', fname)
