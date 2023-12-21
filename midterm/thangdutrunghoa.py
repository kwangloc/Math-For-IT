# Huong dan nhap:
# Nhap so phuong trinh cua he: 3
# a1 = 2
# m1 = 3
# a2 = 3
# m2 = 5
# a3 = 5
# m3 = 7
# -> Nghiem: 278mod105

def main():
    print("Tim nghiem he phuong trinh thang du Trung Hoa")
    k = int(input("Nhap so phuong trinh cua he: "))
    thang_du_trung_hoa(k)

def thang_du_trung_hoa(k):
    ai = [] # List ai chứa các hệ số ai của hệ
    mi = [] # List mi chứa các hệ số mi của hệ
    Mi = [] # List Mi chứa M1, M2,...Mk
    yi = [] # List yi chứa yk là các nghịch đảo module mk của Mk
    M = 1
    x = 0
    # Nhập các phần tử của hệ
    for i in range(0, k):
        ai.append(int(input(f"a{i+1} = ")))
        mi.append(int(input(f"m{i+1} = ")))
        M *= mi[i]
    # List Mi chứa M1, M2,...Mk
    for i in range(k):
        Mi.append(int(M/mi[i]))

    # List yi chứa yk là các nghịch đảo module mk của Mk
    for i in range(0, k):
        yi.append(NghichDaoModule(Mi[i], mi[i]))

    # Tính nghiệm x
    for i in range(0, k):
        x += ai[i]*Mi[i]*yi[i]

    print(f"Nghiem: {x} mod {M} (chua rut gon)")

# Hàm tính nghịch đảo module M của A
def NghichDaoModule(A, M):
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1

if __name__ == "__main__":
    main()