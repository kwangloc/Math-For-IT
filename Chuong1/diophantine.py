# Huong dan nhap  
# a = 7
# b = 11
# c = 13
# -> x = -39+11.0r, y = 26-7.0r

def main():
    print("Tim nghiem phuong trinh Diophantine")
    print("ax + by = c")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    solution = diophantine(a, b, c)
    if solution:
        x, y, gcd = solution
        sub_1 = int(b/gcd)
        sub_2 = int(a/gcd)
        print(f"x = {x}+{sub_1}r, y = {y}-{sub_2}r")
    else:
        print("Phuong trinh khong co nghiem nguyen")

def gcd_euclid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = gcd_euclid(b, a % b)
        return gcd, y, x - (a // b) * y

def diophantine(a, b, c):
    gcd, x0, y0 = gcd_euclid(a, b)
    if c % gcd != 0:
        return None  
    x = x0 * (c // gcd)
    y = y0 * (c // gcd)
    return x, y, gcd

if __name__ == "__main__":
    main()