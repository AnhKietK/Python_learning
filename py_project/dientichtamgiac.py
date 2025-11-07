import math

a = float(input("nhập vào độ dài cạnh thứ nhất: "))
b = float(input("nhập vào độ dài cạnh thứ hai: "))
c = float(input("nhập vào độ dài cạnh thứ ba: "))

if (a+b > c) and (a+c > b) and (b+c > a):
    chuVi = a + b + c
    p = chuVi/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))

    print("diện tích của tam giác là: ", s)
else: 
    print("3 cạnh này không tạo thành tam giác")
