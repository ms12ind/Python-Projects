class Area:
    def area_of_circle(self):
        print("Area Of Circle")
        inp=int(input("Enter Radius of Circle :"))
        ar=3.14*(inp*inp)
        print("Area of Circle is :",ar)

    def area_of_triangle(self):
        print("Area Of Triangle")
        base=int(input("Enter base :"))
        height = int(input("Enter height :"))
        art=0.5*base*height
        print("Area of Triangle is :",art)

    def area_of_square(self):
        print("Area Of Square")
        inp=int(input("Enter side of square :"))
        ars=inp*inp
        print("Area of Circle is :",ars)

    def area_of_rectangle(self):
        print("Area Of Rectangle")
        lenght=int(input("Enter lenght :"))
        breadth = int(input("Enter breadth :"))
        arr=lenght*breadth
        print("Area of Triangle is :",arr)

m1=Area()
m1.area_of_circle()
m1.area_of_triangle()
m1.area_of_square()
m1.area_of_rectangle()

