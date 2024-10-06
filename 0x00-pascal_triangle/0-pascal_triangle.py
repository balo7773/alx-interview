#/usr/bin/python3

def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def pascal_triangle(n):
    '''
    Calculate pascal triangle.
    
    Args:
        n (int): number of n rows of pascal triangle.
    
    Returns:
        list: list of n row triangle
    '''
    store = list()
    
    if n <= 0:
        return store
    
    for a in range(n):
        # outer loop for n rows
        r = 0
        ans = list()
        fact_a = factorial(a)
        while r <= a:
            sub = a - r
            fact_a_r = factorial((sub))
            fact_r = factorial(r)
            store_ans = int(fact_a / ((fact_a_r) * fact_r))
            ans.append(store_ans)
            r += 1
        store.append(ans)
    
    return store
