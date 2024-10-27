def fibonaci(N):
    if N == 1:
        return 1
    elif N == 0:
        return 0
    else:
        return fibonaci(N - 1) + fibonaci(N - 2)

N = int(input())

print(fibonaci(N))