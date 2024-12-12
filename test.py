def fibonacci(n):
    if isinstance(n, int) and n >= 0:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    else:
        raise ValueError("n must be a non-negative integer")
n = 10
if __name__ == "__main__":
    print(fibonacci(n))