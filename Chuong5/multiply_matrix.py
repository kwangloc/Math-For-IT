def main():
    matrix_P = [
        [0.4, 0.6, 0, 0], 
        [0.1, 0.3, 0.4, 0.2], 
        [0, 0.2, 0.8, 0], 
        [0, 0.4, 0.6, 0]   
    ]
    n = 3
    
    result_matrix = matrix_power(matrix_P, n)

    if result_matrix:
        rounded_result_matrix = round_matrix(result_matrix)
        print(f"Ma trận P^{n} (làm tròn đến 3 chữ số hàng thập phân):")
        for row in rounded_result_matrix:
            print(row)

def matrix_power(matrix, n):
    result = matrix.copy()

    for _ in range(n - 1):
        result = multiply_matrices(result, matrix)

    return result

def multiply_matrices(matrix1, matrix2):
    result = []
    
    if len(matrix1[0]) != len(matrix2):
        print("Không thể nhân hai ma trận này.")
        return None
    
    for i in range(len(matrix1)):
        result.append([0] * len(matrix2[0]))
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

def round_matrix(matrix):
    rounded_matrix = []
    
    for row in matrix:
        rounded_row = [round(num, 3) for num in row]
        rounded_matrix.append(rounded_row)
    
    return rounded_matrix

if __name__ == "__main__":
    main()