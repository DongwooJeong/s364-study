xfile = open("mbox-short.txt")
count=0
for x in xfile:
    count+=1
print(count)

xfile=open("mbox-short.txt",'r')
inp=xfile.read()
print(len(inp))