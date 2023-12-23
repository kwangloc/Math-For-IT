import math
# eratosthenes

def main():
    print("Cac SNT trong khoang [M, N] bang sang Eratosthenes")
    m = int(input("Nhap M: "))
    n = int(input("Nhap N: "))
    primesFromMtoN = eratosthenes(m, n)
    closest_to_300 = find_closest_to_300(primesFromMtoN)
    print(f"Số gần với 300 nhất: {closest_to_300}")

def eratosthenes(m, n):
    so_nguyen = [True] * (n + 1)
    so_nguyen[0] = so_nguyen[1] = False
    for i in range(2, int(math.sqrt(n)+1)):
        if so_nguyen[i] == True:
            for j in range(i*2, n+1, i):
                so_nguyen[j] = False 
    print(f"Cac SNT trong khoang [{m},{n}]: ")
    count = 0
    sum = 0    
    for i in range(m, n+1):
        if so_nguyen[i]:
            count += 1
            sum += i

    for i in range(m, n+1):
        if so_nguyen[i]:
            print(i, end=" ")
        
    primesFromMtoN = [i for i in range(m, n + 1) if so_nguyen[i]]    
    print(f"\nSo luong cac SNT trong khoang [{m},{n}]: {count}")
    print(f"Tong cac SNT trong khoang [{m},{n}]: {sum}")
    return primesFromMtoN

def find_closest_to_300(primes):
    closest = primes[0]
    for prime in primes:
        if abs(prime - 300) < abs(closest - 300):
            closest = prime
    return closest

if __name__ == "__main__":
    main()

