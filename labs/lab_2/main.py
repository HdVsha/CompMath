from tabulate import tabulate


x = [i for i in range(10, 80, 10)]
f = [10, 340, 550, 580, 490, 490, 490]
N = len(f) - 1

F = [f]+[[0]*(N-i) for i in range(N)]  # таблица значений f

k = 1
for j in range(1, len(F)):
    for i in range(len(F[j])):
        if (x[i+k] - x[i]) != 0:
            F[j][i] = (F[j-1][i] - F[j-1][i+1]) / (x[i+k] - x[i])
        else:
            print(f"STOP! YOU HAVE EQUAL NODES: {x[i+k]} and {x[i]}")
            exit(0)
    k += 1
    print(tabulate(F, showindex=[f"k={i}" for i in range(N+1)], tablefmt="fancy_grid"))
