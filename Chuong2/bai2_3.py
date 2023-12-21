# vecto riêng và chỉ số riêng
import numpy as np
import math

def jacobi_eigenvalue(A, max_iterations=1000, epsilon=1e-6):
    n = len(A)
    V = [[0.0] * n for _ in range(n)] 
    for i in range(n):
        V[i][i] = 1.0

    for _ in range(max_iterations):
        max_val = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i][j]) > max_val:
                    max_val = abs(A[i][j])
                    p, q = i, j

        if max_val < epsilon:
            break

        theta = 0.5 * math.atan2(2 * A[p][q], A[q][q] - A[p][p])
        c = math.cos(theta)
        s = math.sin(theta)

        for i in range(n):
            temp = A[p][i]
            A[p][i] = c * temp + s * A[q][i]
            A[q][i] = -s * temp + c * A[q][i]
            temp = A[i][p]
            A[i][p] = c * temp + s * A[i][q]
            A[i][q] = -s * temp + c * A[i][q]
            temp = V[i][p]
            V[i][p] = c * temp + s * V[i][q]
            V[i][q] = -s * temp + c * V[i][q]

    eigenvalues = [A[i][i] for i in range(n)]
    eigenvectors = V
    return eigenvalues, eigenvectors
    
def main():
    A = np.array([[10, -9], [4, -2]])
    eigenvalue, eigenvector = jacobi_eigenvalue(A)
    print("Trị riêng :", eigenvalue)
    print("Vector riêng :", eigenvector)

if __name__ == "__main__":
    main()