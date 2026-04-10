def toDigits(n: int, b:int)->list[int]:
    """Convert a positive number n to its digit representation in base b."""
    if n < 0:
        raise ValueError("n must be >= 0 integer")
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        digits.insert(0, n % b)
        n  = n // b
    return digits

def fromDigits(digits: list[int], b:int)->int:
    """Compute the number given by digits in base b."""
    if b <= 1:
        raise ValueError("Base must be greater than 1")
    n = 0
    for d in digits:
        n = b * n + d
    return n