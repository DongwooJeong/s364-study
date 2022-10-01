finput = input("Enter a file name: ")
xfile = open(finput, 'r')
for line in xfile:
    if "(+)" in line:
        injured = line
        print(injured)
        replacement = input("Enter replacement player(ex. 7. Son Heung-min): ")
        with open(finput, 'r') as file:
            data = file.read()
            data = data.replace(injured, replacement+"\n")
        with open(finput, 'w') as file:
            file.write(data)
        print("Player is replaced.\n")
    else:
        continue
print("No more injured player.\n")

print("Below is the updated lineup.\n")
rfile = open(finput, 'r')
for line in rfile:
    print(line)    
  






