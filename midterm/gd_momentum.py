import numpy as np

def main():
    initial_x = -1.0 # điểm bắt đầu
    learning_rate = 0.001
    momentum = 0.5
    N_loops = 1000
    epsilon = 1e-5 # sai số

    min_x, min_value, x_history = gradient_descent_with_momentum(initial_x, learning_rate, momentum, N_loops, epsilon)

    print("Minimum x:", min_x)
    print("Minimum value of f(x):", min_value)

def f(x):
    return 2 * np.log(2 * x**2 + 1) + 9 * x + 3 * np.exp(x**2) - 5

def df(x):
    return (8 * x / (2 * x**2 + 1)) + 9 + 6 * x * np.exp(x**2)

def gradient_descent_with_momentum(initial_x, learning_rate=0.01, momentum=0.9, N_loops=1000, epsilon=1e-6):
    x = initial_x
    x_history = [x]
    velocity = 0  # Tốc độ ban đầu Vo

    for i in range(N_loops):
        gradient = df(x)
        # velocity = momentum * velocity - learning_rate * gradient
        velocity = momentum * velocity + learning_rate * gradient
        x_old = x
        x = x - velocity
        if np.abs(x - x_old) < epsilon:
            print(f"Tìm được x min sau {i+1} vòng lặp.")
            break
        x_history.append(x)

    return x, f(x), x_history

if __name__ == "__main__":
    main()