import numpy as np

def main():
    A = np.array([
            [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5]], dtype=float)
    
    if (not is_hermitian(A)):
        print("Khong phai la ma tran vuong, doi xung")
    else:
        L = phan_ra_cholesky(A)
        print("Ma tran tam giac duoi L:")
        for i in range(len(L)):
            for j in range(len(L)):
                print(L[i][j], end="\t")
            print()

        print("Ma tran tam giac tren L*:")
        for i in range(len(L)):
            for j in range(len(L)):
                print(L[j][i], end="\t")
            print()

# Ham kiem tra ma tran vuong va doi xung (ma tran Hermitian)
def is_hermitian(matrix): 
    return np.allclose(matrix, matrix.conj().T)

def phan_ra_cholesky(A):
    n = len(A)
    L = np.zeros((n, n), dtype=float) # Khoi tao ma tran tam giac duoi L

    for i in range(n):
        for j in range(i + 1):
            if i == j: # tại đường chéo
                sum_of_squares = 0 
                for k in range(j):
                    sum_of_squares += L[i][k] ** 2
                L[i][j] = (A[i][i] - sum_of_squares) ** 0.5
            else:
                sum_of_products = 0
                for k in range(j):
                    sum_of_products += L[i][k] * L[j][k]
                L[i][j] = (A[i][j] - sum_of_products) / L[j][j]

    return L

if __name__ == "__main__":
    main()


