def primes_in_range(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Error")
    if a > b:
        raise ValueError("Error")

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [x for x in range(a, b + 1) if is_prime(x)]

if __name__ == "__main__":
    primes = primes_in_range(1, 10)
    print(primes)
