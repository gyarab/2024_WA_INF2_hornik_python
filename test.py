def fibonnaci(n):
    if isinstance(n, int) and n >= 0:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonnaci(n-1) + fibonnaci(n-2)
    else:
        raise ValueError("n must be a non-negative integer")
    
if __name__ == "__main__":
    print(fibonnaci(1))