finput = input("Enter a file name: ")
xfile=open(finput)
for line in xfile:
    line = line.rstrip()
    if '@' in line:
        print(line.upper())
