# Ma trận nghịch đảo

# Hàm chuyển vị
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Hàm tính ma trận con bằng cách loại bỏ hàng và cột chỉ định.
def matrix_minor(matrix, row, col):
    return [row[:col] + row[col+1:] for row in (matrix[:row] + matrix[row+1:])]

# Hàm tính định thức của ma trận.
def calculate_determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for col in range(len(matrix)):
        determinant += matrix[0][col] * calculate_determinant(matrix_minor(matrix, 0, col))
    return determinant

# Hàm tính ma trận nghịch đảo.
def calculate_inverse(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Ma trận không vuông, không thể tính nghịch đảo")

    # Tính định thức của ma trận gốc
    det = calculate_determinant(matrix)

    # Kiểm tra định thức khác 0 
    if det == 0:
        raise ValueError("Ma trận không có ma trận nghịch đảo")

    n = len(matrix)
    adjugate = []

    for i in range(n):
        row = []
        for j in range(n):
            # Tính ma trận phụ
            minor = calculate_determinant(matrix_minor(matrix, i, j))
            # Đối xứng ma trận phụ
            cofactor = (-1) ** (i + j) * minor
            row.append(cofactor)
        adjugate.append(row)

    # Chuyển vị ma trận phụ để tính ma trận nghịch đảo
    adjugate = transpose_matrix(adjugate)

    # Chia tỷ lệ bằng định thức của ma trận gốc
    inverse = [[element / det for element in row] for row in adjugate]

    return inverse

def main():
    matrix = [
        [1, 0, 3],
        [2, 1, 1],
        [3, 2, 2]
    ]
    inverse_matrix = calculate_inverse(matrix)
    for row in inverse_matrix:
        print(row)

if __name__ == "__main__":
    main()