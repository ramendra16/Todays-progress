
a= float(input("enter first slide of triangle"))
b= float(input("enter second slide of triangle"))
c= float(input("enter third slide of triangle"))

s= (a+b+c)/2

area= (s*(s-a)*(s-b)*(s-c)**0.5)

print("Area of triangle is: ",area)