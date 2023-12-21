import math
# tinh dinh thuc ma tran
def main():
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    B = [[3, 8],
         [4, 6]]
    det_A = determinant(B) 
    print(det_A)

def determinant(matrix):
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    # Laplace
    for j in range(n):
        cofactor_matrix = []
        for i in range(1, n):
            row = [matrix[i][k] for k in range(n) if k != j]
            cofactor_matrix.append(row)
        det += matrix[0][j] * determinant(cofactor_matrix) * (-1) ** j

if __name__ == "__main__":
    main()
