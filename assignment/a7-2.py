fname = input("Enter a file name: ")
xfile = open(fname)
worddict = dict()
lst = list()
for line in xfile:
    line = line.rstrip()
    if line.startswith('From '):
        fromline = line.split(" ")
        lst.append(fromline[2])
for word in lst:
    print(worddict.get(word,0))
    worddict[word] = worddict.get(word,0) + 1
print(worddict)
