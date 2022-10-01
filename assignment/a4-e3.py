from datetime import datetime

egglist = ["2022-10-20","2022-10-21","2022-10-23","2022-10-30"]
eggnum = int(input("Enter the number of the item(from 1 to 4): "))

eggdate = datetime.strptime(egglist[eggnum-1], "%Y-%m-%d")
eggtoday = datetime.now()

eggdiff = str(eggdate-eggtoday)

eggindex = eggdiff.find("days")
print(eggdiff[0:eggindex+4], "until expiration date.")