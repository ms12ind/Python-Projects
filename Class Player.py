class Player:
    def playerData(self):
        self.l1=[]
        self.name=input("Enter Name :")
        self.pid=int(input("Enter ID : "))
        self.matchesPlayed=int(input("Enter Matches Played :"))
        for i in range(self.matchesPlayed):
            self.score=int(input("Enter Score :"))
            self.l1.append(self.score)
    def display(self):
        print(f"Name : {self.name}\nPlayer ID  : {self.pid}\nMatches Played : {self.matchesPlayed}\nScore in all the Matches  {self.l1}")

l2=[]
for i in range(2):
    s1 = Player()
    s1.playerData()
    l2.append(s1)
for i in l2:
    i.display()