import numpy as np

def main():
    initial_x = 0.0
    learning_rate = 0.1
    N_loops = 1000 # số vòng lặp tối đa
    epsilon = 1e-5 # sai số

    min_x, min_value, x_history = gradient_descent(initial_x, learning_rate, N_loops, epsilon)

    print("Minimum x:", min_x)
    print("Minimum value of f(x):", min_value)

def f(x):
    return np.exp(x) + 2 * (x - 1)**2

def df(x):
    return np.exp(x) + 4 * (x - 1)

def gradient_descent(initial_x, learning_rate=0.01, N_loops=1000, epsilon=1e-6):
    x = initial_x
    x_history = [x]

    for i in range(N_loops):
        gradient = df(x)
        x_old = x
        x = x - learning_rate * gradient
        if np.abs(x - x_old) < epsilon:
            print(f"Converged after {N_loops+1} N_loops.")
            break
        x_history.append(x)

    return x, f(x), x_history

if __name__ == "__main__":
    main()