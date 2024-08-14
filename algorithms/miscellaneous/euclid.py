def gcd(a, b):
    """
    Calculates the Greatest Common Divisor (GCD) of two numbers using the
    Euclidean algorithm.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The GCD of the two numbers.
    """
    while b:
        # The loop continues until b becomes 0
        a, b = b, a % b
        # a becomes b, and b becomes the remainder of a divided by b

    return a  # When b becomes 0, a is the GCD
