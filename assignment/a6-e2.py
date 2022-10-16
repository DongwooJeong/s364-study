fname = open("romeo.txt")
words = []
word = []
for line in fname:
    i = line.rstrip().split(" ")
    words.append(i)
for i in words:
    for j in i:
        word.append(j)
word.sort()
print(word)

