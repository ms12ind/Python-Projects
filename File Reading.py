with open("student.txt","r") as b1:
    c=[]
    for i in range(5):
        b=b1.readline()
        m=b.split("  ")
        c.append(m)

    jk=sorted(c,key=lambda x:x[2])
    print("Students in the order of Surname :")
    for i in jk:
        for j in i:
            print(j,end=" ")
    print()
