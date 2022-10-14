#4xonali sonlarning ko'paytmasi

y = int(input("To'rt xonali sonni kiriting: \n>>>"))
a = y//1000 #Butun qismi
b = y%1000 #Qoldiq qismi
c = b//100  #Butun qismi
d = b%100    #Qoldiq qismi
e = d//10
f = d%10
print("a",a)
# print("b",b)
print("c",c)
# print("d",d)
print("e",e)
print("f",f)
s = a*c*e*f
print("Ko'paytmasi:", s)
