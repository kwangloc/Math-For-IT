# Huong dan nhap
# Nhap so nguyen n: 84

import math

def main():
    print("Tim tich huu han cac so nguyen to cua hop so!")
    n = int(input("Nhap so nguyen n: "))
    prime_factors(n)

def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    print(f"{n} =", end=" ")
    for i in range(n+1): # i: 0->n
        if check_prime(i):
            so_mu = 0
            while n % i == 0:
                so_mu += 1
                n /= i
            if so_mu != 0:
                print(f"{i}^{so_mu}.", end="")

if __name__ == "__main__":
    main()
