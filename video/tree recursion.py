def trace(func):
    def wrapper(n, m):
        print(f"Calling {func.__name__}({n}, {m})")
        result = func(n, m)
        print(f"{func.__name__}({n}, {m}) returned {result}")
        return result
    return wrapper

@trace 
def count_partition(n,m):
   if n == 0:return 1
   elif n <0:return 0
   elif m==0:return 0
   else :
      with_m = count_partition(n-m,m)
      without_m = count_partition(n,m-1)
      return with_m + without_m
print(count_partition(5,3))   