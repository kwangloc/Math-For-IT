import math
# perfect number
def main():
    print("In so hoan hao tu 1 toi n")
    n = int(input("Nhap so nguyen n: "))
    list_perfect_number(n)

def check_perfect_number(k):
    sum = 0
    for i in range(1, int(k/2)+1):
        if k % i == 0:
            sum += i
        if sum > k:
            break
    if sum == k:
        return True
    else:
        return False

def list_perfect_number(n):
    for i in range(1, n+1):
        if check_perfect_number(i):
            print(i, end=" ")

if __name__ == "__main__":
    main()
