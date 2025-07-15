def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m==1 and n==1:
       return 1 
    elif m<1 or n<1:
       return 0
    else:
       return paths(m,n-1) + paths(n,m-1)
    
def sums(n, m):
    """Return lists that sum to n containing positive numbers up to m that
    have no adjacent repeats.
    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if n < 0:
        return []
    if n == 0:
        sums_to_zero = []     # The only way to sum to zero using positives
        return [sums_to_zero] # Return a list of all the ways to sum to zero
    result = []
    for k in range(1, m + 1):
        result = result 
        + [[k] + rest for rest in sums(n - k, m) if rest == [] or rest[0] != k]
        """特指上方四行语句"""
    return result
"""只有当满足条件才会创造新的列表元素,可以等价为下面的for循环
    result_list = []
    for rest in sums(n-k, m):
        if rest == [] or rest[0] != k:  # 条件判断
           result_list.append([k] + rest)
"""