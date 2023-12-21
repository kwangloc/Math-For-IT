import math
# eratosthenes

def main():
    print("In tat ca cac SNT be hon N bang sang Eratosthenes")
    n = int(input("Nhap n: "))
    eratosthenes(n)

def eratosthenes(n):
    so_nguyen = []
    for i in range(0, n+1):
        # so_nguyen[i] = True
        so_nguyen.append(True)
    so_nguyen[0] = so_nguyen[1] = False
    for i in range(2, int(math.sqrt(n)+1)):
        if so_nguyen[i] == True:
            for j in range(i*2, n+1, i):
                so_nguyen[j] = False 
    print("Ket qua: ")
    for i in range(n+1):
        if so_nguyen[i]:
            print(i, end=" ")


if __name__ == "__main__":
    main()
