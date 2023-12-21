# Huong dan nhap
# a = 3
# m = 14
# n = 100

def main():
    # a, r, res, d, n
    print("Chuong trinh tinh a^m mod n")
    a = int(input("a = "))
    m = int(input("m = "))
    n = int(input("n = "))
    res = 1
    r = a % n
    while (m > 0):
        if(m & 1):
            res = (res * r) % n
        r = (r * r) % n
        m >>= 1
    print(f"a^m mod n = {res}")

if __name__ == "__main__":
    main()
