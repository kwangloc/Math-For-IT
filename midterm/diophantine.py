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

# ax + by = GCD(a, b)
# return gcd(a,b), x, y
    
# def gcd_euclid(a, b):
#     if b == 0:
#         return a, 1, 0
#     else:
#         gcd, x, y = gcd_euclid(b, a % b)
#         # return gcd, y, x - (a // b) * y
#         return gcd, y, x - int(a / b) * y

def gcd_euclid(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def diophantine(a, b, c):
    gcd, x0, y0 = gcd_euclid(a, b)
    if c % gcd != 0:
        return None  
    x = x0 * (c / gcd)
    y = y0 * (c / gcd)
    return int(x), int(y), gcd

if __name__ == "__main__":
    main()