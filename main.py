def fibonacci(n: int) -> list:
    """Generiert die ersten n Zahlen der Fibonacci-Reihe.
    
    Args:
        n: int  - Anzahl Zahlen, die generiert werden sollen.
    
    Returns:
        list - Liste der n Fibonacci-Zahlen"""
    if not isinstance(n, int):
        raise TypeError("Ganze Zahl erwartet!")
    
    if n < 0:
        raise ValueError("Negative Zahlen nicht erlaubt!")
    elif n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        nums = [1, 1]
        while len(nums) < n:
            nums.append(nums[-1] + nums[-2])
        return nums

    