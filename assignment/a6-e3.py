fname = open("icecream.txt")
item = []
for line in fname:
    item.append(line.rstrip())

print(item)

new = input("enter new item: ")
if new in item:
    print("already in the list")
else:
    item.append(new)
    print("Change updated")

removed = input("enter removed item: ")
if removed in item:
    item.remove(removed)
    print("Change updated")
else:
    print("Item not in the list")

print(item) 

with open('icecream.txt', 'w') as file:
    for i in item:
        file.write(i+'\n')

