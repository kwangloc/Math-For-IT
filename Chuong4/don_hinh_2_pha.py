import numpy as np

def main():
    # Ví dụ min(-2x1 - x2)
    c = np.array([-2, -1])
    A = np.array([[1, 1], 
                [-1, 2], 
                [3, 2]])
    b = np.array([4, 2, 12])
    result = two_phase_simplex(c, A, b)
    print("Nghiệm tối ưu:", result[0])

def two_phase_simplex(c, A, b):
    m, n = A.shape

    # Giai đoạn I
    # Thêm biến giả
    A_phase1 = np.hstack((A, np.eye(m)))
    c_phase1 = np.hstack((np.zeros(n), np.ones(m)))
    x_phase1, tableau_phase1 = simplex_method(c_phase1, A_phase1, b)

    # Kiểm tra khả thi của nghiệm xuất phát
    if x_phase1 is None or not np.allclose(x_phase1[-m:], np.zeros(m)):
        print("Bài toán không có nghiệm khả thi.")
        return None

    # Loại bỏ biến giả và chuyển sang giai đoạn II
    A_phase2 = A
    c_phase2 = c
    x_phase2, tableau_phase2 = simplex_method(c_phase2, A_phase2, b)

    return x_phase2, tableau_phase2

def simplex_method(c, A, b):
    # Bổ sung biến lõi và tạo bảng đơn hình
    B = np.eye(len(b))
    A = np.hstack((A, B))
    c = np.hstack((c, np.zeros(len(b))))

    while True:
        # Tìm cột pivot
        pivot_column = np.argmin(c)

        # Kiểm tra điều kiện dừng
        if c[pivot_column] >= 0:
            break

        # Tìm hàng pivot
        ratios = b / A[:, pivot_column]
        pivot_row = np.argmin(ratios)

        # Thực hiện pivot
        A = pivot(A, pivot_row, pivot_column)
        B[pivot_row] = c[pivot_column]

    x = np.zeros(len(c))
    x[:len(b)] = b

    # Xây dựng bảng đơn hình cuối cùng
    tableau = {'tableau': A, 'basis': np.where(B)[0], 'solution': x}

    return x, tableau

def pivot(A, row, col):
    pivot_element = A[row, col]

    if pivot_element == 0:
        print("Bài toán không có nghiệm tối ưu hoặc có vô số nghiệm.")
        return A

    A[row, :] /= pivot_element

    for i in range(len(A)):
        if i != row:
            A[i, :] -= A[i, col] * A[row, :]

    return A


if __name__ == '__main__':
    main()