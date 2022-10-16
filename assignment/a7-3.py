salesdict = dict()
fname = open("sales.txt")
for line in fname:
    line = line.rstrip()
    splitline = line.split(" ")
    salesdict[int(splitline[0])] = splitline[1]


method = input("Please indicate (Create, Read, Update, Delete) : ")
if method == "Create":
    createkey = int(input("Enter year: "))
    if int(createkey) in salesdict:
        print("Following year is already in the list")
    else:
        createval = input("Enter sales amount: ")
        salesdict[int(createkey)] = createval

elif method == "Read":
    print(salesdict)

elif method == "Update":
    updatekey = int(input("Enter year: "))
    if int(updatekey) not in salesdict:
        print("Following year is not in the list")
    else:
        updateval = input("Enter sales amount: ")
        salesdict[int(updatekey)] = updateval

elif method == "Delete":
    deletekey = int(input("Enter year: "))
    if int(deletekey) not in salesdict:
        print("Following year is not in the list")
    else:
        del salesdict[int(deletekey)]

else:
    print("Please select among (Create, Read, Update, Delete)")

with open("sales.txt", 'w') as file:
    for key, value in dict(sorted(salesdict.items())).items():
        file.write('%s %s\n' % (key, value))
file.close()