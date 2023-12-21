# phân rã ma trận thành vecto riêng và chỉ số riêng
import numpy as np

A = np.array([[2, -1], [-1, 3]])
eigenvalues, eigenvectors = np.linalg.eig(A)

# In kết quả
for i in range(len(eigenvalues)):
    eigenvalue = eigenvalues[i]
    eigenvector = eigenvectors[:, i]  # Lấy vector riêng tương ứng với trị riêng thứ i
    print(f"Trị riêng {i + 1}: {eigenvalue}")
    print(f"Vector riêng {i + 1}:", eigenvector)
    print()
