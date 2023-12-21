# Huong dan nhap
# Nhap so nguyen a: 1804
# Nhap so nguyen b: 328
# -> GCD(a,b) =  164

import math
# Euclid
def main():
    print("Tim UCLN bang thuat toan Euclid")
    a = int(input("Nhap so nguyen a: "))
    b = int(input("Nhap so nguyen b: "))
    gcd = gcd_euclid(a, b)
    print("GCD(a,b) = ", gcd)

def gcd_euclid(a, b):
    print(f"a: {a}, b: {b}")
    if (b == 0):
        return a
    return gcd_euclid(b, a%b)

if __name__ == "__main__":
    main()
