class Myclass:
    def listComp(self):
        vow=["a","e","i","o","u"]
        fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

        # l2=[]
        # l1=[j if j in vow else l2.append(j)   for i in fruits for j in i]

        # print(l1)
        m1=[]
        for i in fruits:
            count=0
            for j in i:
                if j in vow:
                    count+=1
            if count>2:
                m1.append(i)

        print(m1)



m1=Myclass()
m1.listComp()

