import numpy as np
nprow = int(input("enter the number of restaurants you are going to evaluate: "))
list = []
for i in range(nprow):
    print("evaluate the restaurant")
    taste =  int(input("how delicious: "))
    list.append(taste)
    visual = int(input("how good looking: "))
    list.append(visual)
    price = int(input("how expensive: "))
    list.append(price)

matrix = np.array(list)

score = matrix.reshape(nprow,3)

wvalue = np.array([8,6,5])

rating = np.dot(score,wvalue)
print(rating)