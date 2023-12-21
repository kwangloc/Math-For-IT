import numpy as np

def cholesky_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i+1):
            if i == j:
                sum_sq = sum(L[i][k] ** 2 for k in range(j))
                L[i][j] = np.sqrt(A[i][i] - sum_sq)
            else:
                sum_Lik_Ljk = sum(L[i][k] * L[j][k] for k in range(j))
                L[i][j] = (A[i][j] - sum_Lik_Ljk) / L[j][j]

    return L

def main():
    A = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]])
    L = cholesky_decomposition(A)
    print("Ma trận tam giác dưới L:")
    print(L)

if __name__ == "__main__":
    main()