# Huong dan nhap:
# Nhap so phuong trinh cua he: 3
# a1 = 2
# m1 = 3
# a2 = 3
# m2 = 5
# a3 = 5
# m3 = 7
# -> sol = 68mod105

def main():
    print("Tim nghiem he phuong trinh thang du Trung Hoa")
    k = int(input("Nhap so phuong trinh cua he: "))
    thang_du_trung_hoa(k)

def thang_du_trung_hoa(k):
    ai = []
    mi = []
    Mi = []
    yi = []
    M = 1
    # Nhap cac phan tu cua he
    for i in range(k):
        ai.append(int(input(f"a{i+1} = ")))
        mi.append(int(input(f"m{i+1} = ")))
        M *= mi[i]
    for i in range(k):
        Mi.append(int(M/mi[i]))
    for i in range(k):
        yi.append(inverseModule(Mi[i], mi[i]))

    sol = 0
    for i in range(k):
        sol += ai[i]*Mi[i]*yi[i]

    res = sol%M
    print(f"Nghiem: x={res}+{M}k, k thuoc Z")

def inverseModule(A, M): 
    for X in range(1, M): 
        if (((A % M) * (X % M)) % M == 1): 
            return X 
    return -1

if __name__ == "__main__":
    main()