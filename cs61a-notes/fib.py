def fib1(n):
    """Compute the nth Fibonacci number"""
    pred, curr = 0, 1
    k = 1
    while k < n:
        print(f"pred: {pred}, curr: {curr}, k: {k}")
        pred, curr = curr, pred + curr
        k += 1
    return curr

def fib2(n):
    """Compute the nth Fibonacci number"""
    pred, curr = 1, 0
    k = 0
    while k < n:
        print(f"pred: {pred}, curr: {curr}, k: {k}")
        pred, curr = curr, pred + curr
        k += 1
    return curr

def compare_fibs(n):
    """Compares fib values for values upto an integer N"""
    print(f"n is {n}. Fib1: {fib1(n)}, Fib2: {fib2(n)}")
