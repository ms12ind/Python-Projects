myDict={}
for i in range(0,2):
    name=input("Enter name :")
    m1=int(input("Enter Marks : "))
    m2 = int(input("Enter Marks : "))
    m3 = int(input("Enter Marks : "))
    myDict[name]=[m1,m2,m3]
print(myDict)
myDict.update({'Sameer':[34,34,34]})
print(myDict)
