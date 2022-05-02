import numpy as np
import matplotlib.pyplot as plt


# Given intervals
a = 0
b = [1, 3]
y_0 = 1
y_b = -1
# Given steps
h = [0.02, 0.01, 0.005]


for b_el in b:
    y_arrays = []
    x_arrays = []
    length = b_el - a
    for h_el in h:
        N = int(length / h_el)
        # Create matrix of zeros of given size (remember about already given 2 dots)
        A = np.zeros([N + 1, N + 1])

        # Create respective vector of x (remember about already given 2 dots) with a step of h
        x = np.linspace(a, b_el, num=N+1, endpoint=True)

        # Create vector of free coefficients

        d = [y_0] + [pow(h_el, 2) * np.exp(x[k]) * np.sin(2 * x[k]) for k in range(1, len(x)-1)] + [y_b]

        '''
        Straight move
        '''

        # Computing A matrix with 3 diagonals
        # e.g.
        # 1 0 0 0 0
        # 1 2 1 0 0
        # 0 1 5 1 0
        # 0 0 1 8 1
        # 0 0 0 0 1

        for i in range(N + 1):
            for j in range(N + 1):
                if i == j == 0 or i == j == N:
                    A[i][j] = 1
                elif i == j != 0 or i == j != N:
                    A[i][j] = 1 + h_el
                    A[i][j - 1] = 1 - h_el
                    A[i][j + 1] = 5 * pow(h_el, 2) - 2
        # Now everything resembles us of A*y = b
        # So let's find out y vector

        '''
        Reverse move
        '''

        # Let's just solve the system A*y = d with the help of gorgeous mother np.linalg.solve   :D
        y = np.linalg.solve(A, d)
        y_arrays.append(y)
        x_arrays.append(x)

    fig1 = plt.figure(figsize=(16, 8))
    ax1 = fig1.add_subplot(1, 2, 1)
    ax1.set_title("Результаты метода для различных b и h")
    ax1.plot(x_arrays[0], y_arrays[0], 'k',
             label=rf"При b={b_el} и h={h[0]}")
    ax1.plot(x_arrays[1], y_arrays[1], 'r',
             label=rf"При b={b_el} и h={h[1]}")
    ax1.plot(x_arrays[2], y_arrays[2], 'g',
             label=rf"При b={b_el} и h={h[2]}")

    ax1.set_ylabel('y')
    ax1.set_xlabel('x')
    ax1.grid(True)
    ax1.legend()


