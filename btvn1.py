tong_tien = int(input("Nhập tổng số tiền hóa đơn (VND): "))

if tong_tien >= 500000:
    phan_tram_giam = 10
    tien_giam = tong_tien * 10 // 100
else:
    phan_tram_giam = 0
    tien_giam = 0

tien_phai_tra = tong_tien - tien_giam

print(f"Số tiền giảm      : {tien_giam:,} VND")
print(f"Tiền phải trả     : {tien_phai_tra:,} VND")