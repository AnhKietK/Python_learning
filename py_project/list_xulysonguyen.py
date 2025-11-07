# Bài tập: Xử lý danh sách số nguyên
# Viết chương trình thực hiện các yêu cầu sau:
# Nhập vào một danh sách các số nguyên từ bàn phím (các số cách nhau bởi dấu cách).
# In ra:
# Danh sách ban đầu.
# Tổng các phần tử trong danh sách.
# Phần tử lớn nhất và nhỏ nhất.
# Danh sách sau khi loại bỏ các phần tử trùng lặp.
# Danh sách sau khi sắp xếp tăng dần.

soNguyenList = list(map(int, input("Nhập danh sách: ").split()))

print("Danh sách ban đầu:", soNguyenList)

tong = sum(soNguyenList)
lon_nhat = max(soNguyenList)
nho_nhat = min(soNguyenList)

print("Tổng:", tong)
print(f"Lớn nhất: {lon_nhat}, Nhỏ nhất: {nho_nhat}")

# Loại trùng
khong_trung = list(dict.fromkeys(soNguyenList))
print("Không trùng:", khong_trung)

# Sắp xếp tăng dần
sap_tang = sorted(soNguyenList)
print("Tăng dần:", sap_tang)
