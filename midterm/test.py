import numpy as np

def markov_chain_probability(P, ql, qk, n):
    P_n = np.linalg.matrix_power(P, n)
    return P_n[ql, qk]

# Ví dụ sử dụng
P = np.array([
    [0.4, 0.6, 0, 0], 
    [0.1, 0.3, 0.4, 0.2], 
    [0, 0.2, 0.8, 0], 
    [0, 0.4, 0.6, 0]]   
)

ql = 1  # Trạng thái ban đầu
qk = 3  # Trạng thái muốn đạt được
n = 3   # Số bước

probability = markov_chain_probability(P, ql, qk, n)
print(f"Xác suất chuyển từ trạng thái {ql} đến trạng thái {qk} sau {n} bước là: {probability}")
