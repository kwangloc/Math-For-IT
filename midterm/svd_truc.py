import numpy
import math

def phan_ra_svd(A):
    A = numpy.array(A, dtype=float)

    AT = []  # AT la ma tran chuyen vi cua A
    for i in range(len(A)):
        row = []
        for j in range(len(A)):
            row.append(A[j][i])
        AT.append(row)

    AT = numpy.array(AT, dtype=float)
    A2 = numpy.matmul(AT, A)  # A2=AT.A
    A2 = numpy.array(A2, dtype=float)

    # Giá trị riêng E, vector riêng V
    E, V = numpy.linalg.eig(A2)  
    E = numpy.array(E, dtype=float)
    E = numpy.flip(E, axis=0)
    V = numpy.array(V, dtype=float)

    for i in range(len(V)):
        V[i] = V[i].round(3)

    E1 = []
    for i in range(len(E)):
        if numpy.isclose(E[i], 0):
            continue
        else:
            E1.append(math.sqrt(E[i]))

    
    
    E1 = numpy.array(E1, dtype=float)
    E1 = numpy.flip(E1, axis=0)
    # Ma trận chéo hóa
    D = []  
    for i in range(len(E1)):
        row = []
        for j in range(len(E1)):
            if i == j:
                row.append(E1[i])
            else:
                row.append(0)
        D.append(row)

    # Ma trận vector riêng trái
    U = []
    for i in range(len(E1)):
        U.append(numpy.dot(A, V[i]) / E1[i])

    U = numpy.array(U, dtype=float)

    print("\nA=UDV^T")
    print("Ma tran U:")
    for row in U:
        for col in row:
            print(round(col, 3), end=" ")
        print()
        

    print("\n\nMa tran D:")
    for i in range(len(D)):
        for j in range(len(D)):
            print(round(D[j][i], 3), end="\t")
        print()


    for i in range(len(A)):
        for j in range(i, len(A)):
            t = V[i][j]
            V[i][j] = V[j][i]
            V[j][i] = t

    print("\n\nMa tran V^T:")
    for i in range(len(V)):
        for j in range(len(V)):
            print(round(V[j][i], 3), end="\t")
        print()

def main():
    # A = [
    #     [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 2],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5]
    # ]
    A = [
        [1, -0.8],
        [0, 1],
        [1, 0]
    ]
    print("Ma tran A:")
    for i in range(len(A)):
        for j in range(len(A)):
            print(A[j][i], end="\t")
        print()
    phan_ra_svd(A)
        
            
if __name__ == "__main__":
    main()