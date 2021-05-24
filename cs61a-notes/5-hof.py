def repeat(f, x):
    while f(x) != x:
        x = f(x)
    return x

def g(y):
    return (y + 5) // 3



def outer(prev_leader=None):
    """
    Recreating the commentary higher-order functions in the Hog project.
    When the outer function is called, it returns the inner function.
    The result of the outer function has to be called with two arguments which prints 
    and returns a new outer function.
    
    >>> f0 = outer()
    >>> f1 = f0(1, 2)
    leader: 1
    
    """
    
    def inner(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        print(f"leader: {leader}")
        return outer(leader)
    return inner
