student = [ "Bé Uyên", "Uyên", "Uyên", "Mèo", "An"]

print("Vị trí số 1 của list: ", student[1]) #in ra vị trí số 1 là Be

print("in ra vị trí số 1 kết thúc ở số 3", student[1:3]) #in ra vị trí số 1 kết thúc ở số 3 là Be và Uyên

student.append("Kiệt") # thêm Kiệt vào cuối list

student.insert(2, "Nhũi") # thêm Nhũi vào vị trí số 2

print(len(student)) # in độ dài list

print("đếm có mấy bé Uyên:", student.count("Uyên"))

# xóa theo phần tử
if "An" in student:
     student.remove("An")

# xem kiểu dữ liệu
print("student là: ", type(student))


# xóa theo vị trí
student.pop(2)

# đảo ngược list
student.reverse()

# sắp xếp list
student.sort()

# sắp xếp ngược
student.sort(reverse=True)

# xóa hết dữ liệu list
# student.clear()

# duyệt list theo phần tử
for x in student:
     print(x)

# duyệt list theo vị trí
for i in range(len(student)):
     print(student[i])

student.append("An")

# tạo danh sách mới không có phần tử nào đó
newlist = [x for x in student if x != "An"]

print(newlist)

entry = list(input("Enter the values: ").split(","))
# User enters: 1,2,3,4,5
# List ends up as: [1, 2, 3, 4, 5]
print(entry)

# If our list contains mixed data types (like integers and strings) then we need to convert each element to a string before joining them
# .By using map(), we can efficiently apply the conversion to every item in the list in a clear and simple manner
a = [1, 2, 3, 4, 5]
print(' '.join(map(str, a)))