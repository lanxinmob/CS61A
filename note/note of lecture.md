## Lecture7.Function Examples
```python
def repeat(k):
    return  detector(lambda j:Flase)(k)

def detector(have_seen_i_before):
    def g(i):
        if have_seen_i_before(i):
           print(i)
        return detector(lambda j:j == i )
    return g

repeat(1)(7)(7)
"""
前一个输入的数字为i，后一个输入的数字为j
"""
```

```python
pumbaa = lambda f: lambda x:f(f(x))
pumbaa = pumbaa(pumbaa)
"""
也就是会进行四次作为argument的函数 
"""
```
## Lecture 9.Tree Recursion
![[QQ_1741431862695.png]]
![[QQ_1741431966039.png]]
## Lecture14. Iterators
- ```python
  s = [1,2,4]
  t = iter(s)
  next(t)
  >>> 1
  next(t)
  >>> 2
  next(t)
  >>> 4
  next(t)
  StopIteration
  >>> next(iter(s))
  1
  >>> next(iter(s))
  1
  ```
- ```PYTHON
   S = {'A': 1 ,'B': 4 }
   iter(S.keys())
   iter(S.values())
   iter(S.items())
  ```
  字典迭代器中间不能改变字典的`size`，但可以改变值，如`S['A'] = 2`,不然就要生成新的迭代器。

- ```python
  >>> for i in iter(range(3,6)):
  ...     print(i)
  ...
  3
  4
  5
  >>> for i in iter(range(3,6)):
  ...     print(i)
  ...
  3
  4
  5
  t = iter(range(3,6))
  >>> for i in t:
  ...     print(i)
  ...
  3
  4
  5
  >>> for i in t:
  ...     print(i)
  ...
  >>> 
  ```
## 小结
- 由上面几个我们可以清楚地看出迭代器的**一次性消耗特性**。每次使用同一个迭代器会耗尽，每次使用新创建的迭代器就不会。
### 内置函数
- 惰性求值：不会立即计算而是返回一个迭代器对象
- `map(func, iterable)`将函数 func 应用于 iterable 中的每一个元素。
- `filter(func, iterable)`根据函数 func 来过滤 iterable 中的元素。
- `zip(a,b)` 将一个或多个可迭代对象的对应元素“拉链式”地打包成一个个元组。
  ```python
  students = ['Alice', 'Bob', 'Charlie']
  scores = [95, 88, 92]
  t = zip(students,scores)
  #[('Alice', 95), ('Bob', 88), ('Charlie', 92)]
  ```
- `reversed(sequence)` 将序列反转返回一个迭代器。
#### 迭代器转换为容器
- 将可迭代对象的所有元素取出，放入列表或元组。
- `list(iterable)`
- `tuple(iterable)`
- `sorted(iterable)` (从小到大)
## Lecture15. Generator
- 生成器就是一种特殊的迭代器
- ```python
  def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k-1)
        """这句就相当于
        for k in coutdown(k-1)
            yield k
        """
    else:
        yield 'Blast off'

    result = list(countdown(5))
    print(result)
    [5, 4, 3, 2, 1, 'Blast off']
  ```
- ```python
    def prefixes(s):
        if s:
            yield from prefixes(s[:-1])
            yield s

    result = list(prefixes('cat'))
    print(result)

    ['c', 'ca', 'cat']

    def substrings(s):
        if s:
            yield from prefixes(s)
            yield from substrings(s[1:])

    result = list(substrings('cat'))
    print(result)
    
    ['c', 'ca', 'cat', 'a', 'at', 't']
  ```
- 分割数字`n`为最大元素不超过`m`
  ```python
  def partitions_as_list(n, m):
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [[m]] 
        with_m = [p + [m] for p in partitions_as_list(n - m, m)]
        without_m = partitions_as_list(n, m - 1)
        
        return exact_match + with_m + without_m

    [2, 4]
    [1, 1, 4]
    [3, 3]
    [1, 2, 3]
    [1, 1, 1, 3]
    [2, 2, 2]
    [1, 1, 2, 2]
    [1, 1, 1, 1, 2]
    [1, 1, 1, 1, 1, 1]
  ```
  ```python
  def partitions_with_spaces(n, m):
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [str(m)]
        with_m = [p + '+' + str(m) for p in partitions_with_spaces(n - m, m)]
        without_m = partitions_with_spaces(n, m - 1)
        
        return exact_match + with_m + without_m


    for p in partitions_with_spaces(6, 4):
        print(p)
    2+4
    1+1+4
    3+3
    1+2+3
    1+1+1+3
    2+2+2
    1+1+2+2
    1+1+1+1+2
    1+1+1+1+1+1
  ```
  前面两个都要消耗大量的内存，而使用生成器就可以不用存储所有可能的结果，只在内存中处理当前的一条路径。
  ```python
  def partitions_(n, m):
    if n>0 and m>0:
        if n == m:
            yield str(m)
        for p in partitions_(n - m, m):
            yield  p+ '+' + str(m)
        yield from partitions_(n, m - 1)
  ```
- 需要注意`yield from`不参与计算，只是委托后面生成器将任务执行完毕并把结果转发出来。
## OOP
- ```python 
  def repr(x):
  return type(x).__repr__(x)
  ```
  通过类来获取类中定义的`__repr__`方法
- ```python
  def gcd(n, d):
      while n != d:
          n, d = min(n, d), abs(n-d)
      return n

  class Ratio:      
      def __init__(self, n, d):
          self.numer = n
          self.denom = d

      def __repr__(self):
          return 'Ratio({0}, {1})'.format(self.numer, self.denom)

      def __str__(self):
          return '{0}/{1}'.format(self.numer, self.denom)

      def __add__(self, other):
          if isinstance(other, int):
              n = self.numer + self.denom * other
              d = self.denom
          elif isinstance(other, Ratio):
              n = self.numer * other.denom + self.denom * other.numer
              d = self.denom * other.denom
          elif isinstance(other, float):
              return float(self) + other
              
          g = gcd(n, d)
          return Ratio(n//g, d//g)

      __radd__ = __add__

      def __float__(self):
          return self.numer / self.denom
  ```
## Efficiency
### Measuring Efficiency !!!
- ```python
  def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

  def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

  fib = count(fib)
  """需要注意这个时候fib已经变成了初始化好的counted，等待n的传入，
  counted中的f依然指向fib，但是fib中fib已经变成了counted。
  """
  result = fib(5) 
  5
  fib.call_cout
  15
  ```
### Memoization
- ```python
  def memo(f):
      cache = {}
      def  memoized(n):
         if n not in cache:  
            cache[n] = f(n)
         return cache[n]
      return memoized
  ``` 
### Composition
#### Tree Class
- ```python
  def indented(self):
      line = []
      for b in self.branches():
        for c in b.indented():
           line.append(' ',c)
    return [str(self.label)]+line
 
  def __str__(self):
    return '\n'.join(self.indented())
    """也就是用换行来分割各个已缩进好的字符串
    """
  ```