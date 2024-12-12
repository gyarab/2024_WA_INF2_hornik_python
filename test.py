def is_prime(number):

    if not isinstance(number, int) or number <= 0:
        raise ValueError("Zadejte realne cislo vetsi nez 0")

    if number == 1:
        return False 
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

# Příklad použití:
try:
    print(is_prime(7))  
    print(is_prime(10))  
    print(is_prime(-5))  
except ValueError as e:
    print(e)