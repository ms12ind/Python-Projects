import sqlite3
class Mydb:
    def Exec(self):
        conn = sqlite3.connect("Q3.db")
        c = conn.cursor()

        #Table Creation
        # c.execute("""CREATE TABLE Dept(dept_ID int(20),name varchar(20),hod varchar(20),staff varchar(20))""")
        #
        # c.execute("""CREATE TABLE Employee(emp_ID int(20),name varchar(20),salary int(20),address varchar(20))""")
        #
        # c.execute("""CREATE TABLE Attendance(emp_ID int(20),present_Days int(20),leaves int(20))""")

        # c.execute("INSERT INTO Dept VALUES ('101','Manas','Technical','clerk')")

        # c.execute("INSERT INTO Dept VALUES ('102','HR','Aditya','clerk')")
        # c.execute("INSERT INTO Dept VALUES ('103','Sales','Anand','racc')")
        # c.execute("SELECT * FROM Dept")
        # print(c.fetchall())

        # c.execute("INSERT INTO Employee VALUES (1,'Alan',55000,'Baner')")
        # c.execute("INSERT INTO Employee VALUES (2,'rudra',45000,'Kothrud')")
        # c.execute("INSERT INTO Employee VALUES (3,'Ram',75000,'Penn')")

        # c.execute("INSERT INTO Attendance VALUES (1,300,65)")
        # c.execute("INSERT INTO Attendance VALUES (2,290,75)")
        # c.execute("INSERT INTO Attendance VALUES (3,310,55)")

        c.execute("SELECT * FROM Employee WHERE salary>50000 ")
        print(c.fetchall())

        c.execute("SELECT * FROM Attendance WHERE present_Days>=300 ")
        print(c.fetchall())

        c.execute("SELECT * FROM Dept WHERE staff='clerk' ")
        print(c.fetchall())

        c.execute("DELETE  FROM Attendance WHERE emp_ID=2 ")
        print(c.fetchall())
        c.execute("DELETE  FROM Dept WHERE staff='clerk' ")
        print(c.fetchall())





        conn.commit()
        conn.close()

s1=Mydb()
s1.Exec()