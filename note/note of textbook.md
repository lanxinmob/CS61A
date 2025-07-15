## ch1.1
 Python has built-in support for a wide range of common programming activities, such as manipulating text, displaying graphics, and communicating over the Internet. The line of Python code
 
```python
>>> from urllib.request import urlopen
```
is an import statement that loads functionality for accessing data on the Internet. In particular, it makes available a function called urlopen, which can access the content at a uniform resource locator ([[URL]]), a location of something on the Internet.
Learning to interpret errors and diagnose the cause of unexpected errors is called _debugging_. Some guiding principles of debugging are:

1. **Test incrementally**: Every well-written program is composed of small, modular components that can be tested individually. Try out everything you write as soon as possible to identify problems early and gain confidence in your components.
2. **Isolate errors**: An error in the output of a statement can typically be attributed to a particular modular component. When trying to diagnose a problem, trace the error to the smallest fragment of code you can before trying to correct it.
3. **Check your assumptions**: Interpreters do carry out your instructions to the letter — no more and no less. Their output is unexpected when the behavior of some code does not match what the programmer believes (or assumes) that behavior to be. Know your assumptions, then focus your debugging effort on verifying that your assumptions actually hold.
4. **Consult others**: You are not alone! If you don't understand an error message, ask a friend, instructor, or search engine. If you have isolated an error, but can't figure out how to correct it, ask someone else to take a look. A lot of valuable programming knowledge is shared in the process of group problem solving.

**Incremental testing, modular design, precise assumptions, and teamwork** are themes that persist throughout this text. Hopefully, they will also persist throughout your computer science career.
## ch1.2
While `print` and `abs` may appear to be similar in these examples, they work in fundamentally different ways. The value that print returns is always `None,` a special Python value that represents nothing. The interactive Python interpreter does not automatically print the value None.
A nested expression of calls to `print` highlights the non-pure character of the function.
```PYTHON
>>> print(print(1), print(2))
1
2
None None
```
## ch1.3
The // operator, on the other hand, rounds the result down to an integer:
```python
>>> 5 // 4
1
>>> -5 // 4
-2
```
These two operators are shorthand for the truediv and floordiv functions.
```python
>>> from operator import truediv, floordiv
>>> truediv(5, 4)
1.25
>>> floordiv(5, 4)
1
```
## ch1.4
- ***Don't repeat yourself*** is a central tenet of software engineering. The so-called DRY principle states that multiple fragments of code should not describe redundant logic. Instead, that logic should be implemented once, given a name, and applied multiple times.
-  ==Decomposing a complex task into concise functions is a skill that takes experience to master.== Fortunately, Python provides several features to support your efforts.
## ch1.5
### 1.5.6
**Assertions.** Programmers use `assert` statements to verify expectations, such as the output of a function being tested. An `assert` statement has an expression in a boolean context, followed by a quoted line of text (single or double quotes are both fine, but be consistent) that will be displayed if the expression evaluates to a false value.
```python
>>> assert fib(8) == 13, 'The 8th Fibonacci number should be 13'
```
When the expression being asserted evaluates to a true value, executing an assert statement has no effect. When it is a false value, `assert` causes an error that halts execution.

A test function for `fib` should test several arguments, including extreme values of n.
```python
>>> def fib_test():
        assert fib(2) == 1, 'The 2nd Fibonacci number should be 1'
        assert fib(3) == 1, 'The 3rd Fibonacci number should be 1'
        assert fib(50) == 7778742049, 'Error at the 50th Fibonacci number'
```
When writing Python in files, rather than directly into the interpreter, tests are typically written in the same file or a neighboring file with the suffix _test.py.

**Doctests.** Python provides a convenient method for placing simple tests directly in the docstring of a function. The first line of a docstring should contain a one-line description of the function, followed by a blank line. A detailed description of arguments and behavior may follow. In addition, the docstring may include a sample interactive session that calls the function:
```python
>>> def sum_naturals(n):
        """Return the sum of the first n natural numbers.

        >>> sum_naturals(10)
        55
        >>> sum_naturals(100)
        5050
        """
        total, k = 0, 1
        while k <= n:
            total, k = total + k, k + 1
        return total
```
Then, the interaction can be verified via the [doctest module](http://docs.python.org/py3k/library/doctest.html). Below, the `globals` function returns a representation of the global environment, which the interpreter needs in order to evaluate expressions.
```python
>>> from doctest import testmod
>>> testmod()
TestResults(failed=0, attempted=2)
```

To verify the doctest interactions for only a single function, we use a `doctest` function called `run_docstring_examples`. This function is (unfortunately) a bit complicated to call. Its first argument is the function to test. The second should always be the result of the expression `globals(),` a built-in function that returns the global environment. The third argument is `True` to indicate that we would like "verbose" output: a catalog of all tests run.
```python
>>> from doctest import run_docstring_examples
>>> run_docstring_examples(sum_naturals, globals(), True)
Finding tests in NoName
Trying:
    sum_naturals(10)
Expecting:
    55
ok
Trying:
    sum_naturals(100)
Expecting:
    5050
ok
```

When the return value of a function does not match the expected result, the run_docstring_examples function will report this problem as a test failure.

When writing Python in files, all doctests in a file can be run by starting Python with the doctest command line option:
```python
python3 -m doctest -v <python_source_file>
```
## ch1.6
### 1.6.3
Hence, we realize two key advantages of lexical scoping in Python.

- The names of a local function do not interfere with names external to the function in which it is defined, because the local function name will be bound in the current local environment in which it was defined, rather than the global environment.
- A local function can access the environment of the enclosing function, because the body of the local function is evaluated in an environment that extends the evaluation environment in which it was defined.
### 1.6.6   Currying
We can use higher-order functions to convert a function that takes multiple arguments into a chain of functions that each take a single argument. More specifically, given a function f(x, y), we can define a function g such that g(x)(y) is equivalent to f(x, y). Here, g is a higher-order function that takes in a single argument x and returns another function that takes in a single argument y. This transformation is called _currying_.

As an example, we can define a curried version of the pow function:
```python
>>> def curried_pow(x):
        def h(y):
            return pow(x, y)
        return h

>>> curried_pow(2)(3)
8
```

Some programming languages, such as Haskell, only allow functions that take a single argument, so the programmer must curry all multi-argument procedures. In more general languages such as Python, currying is useful when we require a function that takes in only a single argument. For example, the _map_ pattern applies a single-argument function to a sequence of values. In later chapters, we will see more general examples of the map pattern, but for now, we can implement the pattern in a function:
```python
>>> def map_to_range(start, end, f):
        while start < end:
            print(f(start))
            start = start + 1

```

We can use map_to_range and curried_pow to compute the first ten powers of two, rather than specifically writing a function to do so:
```python
>>> map_to_range(0, 10, curried_pow(2))
1
2
4
8
16
32
64
128
256
512
```


We can similarly use the same two functions to compute powers of other numbers. Currying allows us to do so without writing a specific function for each number whose powers we wish to compute.

In the above examples, we manually performed the currying transformation on the pow function to obtain curried_pow. Instead, we can define functions to automate currying, as well as the inverse _uncurrying_ transformation:
```python
>>> def curry2(f):
        """Return a curried version of the given two-argument function."""
        def g(x):
            def h(y):
                return f(x, y)
            return h
        return g

>>> def uncurry2(g):
        """Return a two-argument version of the given curried function."""
        def f(x, y):
            return g(x)(y)
        return f

>>> pow_curried = curry2(pow)
>>> pow_curried(2)(5)
32
>>> map_to_range(0, 10, pow_curried(2))
1
2
4
8
16
32
64
128
256
512
```

The curry2 function takes in a two-argument function f and returns a single-argument function g. When g is applied to an argument x, it returns a single-argument function h. When h is applied to y, it calls f(x, y). Thus, curry2(f)(x)(y) is equivalent to f(x, y). The uncurry2 function reverses the currying transformation, so that uncurry2(curry2(f)) is equivalent to f.
```python
>>> uncurry2(pow_curried)(2, 5)
32
```
### 1.6.7   Lambda Expressions
So far, each time we have wanted to define a new function, we needed to give it a name. But for other types of expressions, we don't need to associate intermediate values with a name. That is, we can compute a*b + c*d without having to name the subexpressions a*b or c*d, or the full expression. In Python, we can create function values on the fly using lambda expressions, which evaluate to unnamed functions. A [[lambda]] expression evaluates to a function that has a single return expression as its body. Assignment and control statements are not allowed.
```python
>>> def compose1(f, g):
        return lambda x: f(g(x))
```

We can understand the structure of a lambda expression by constructing a corresponding English sentence:
```python
lambda x : f(g(x))
```
"A function that    takes `x`    and returns     `f(g(x))`"

The result of a lambda expression is called a lambda function. It has no intrinsic name (and so Python prints <[[lambda]]> for the name), but otherwise it behaves like any other function.
```PYTHON
>>> s = lambda x: x * x
>>> s
<function <lambda> at 0xf3f490>
>>> s(12)
144
```

In an environment diagram, the result of a lambda expression is a function as well, named with the greek letter λ (lambda). Our compose example can be expressed quite compactly with lambda expressions.
Some programmers find that using unnamed functions from lambda expressions to be shorter and more direct. However, compound lambda expressions are notoriously illegible, despite their brevity. The following definition is correct, but many programmers have trouble understanding it quickly.
```PYTHON
>>> compose1 = lambda f,g: lambda x: f(g(x))
```

The term _lambda_ is a historical accident resulting from the incompatibility of written mathematical notation and the constraints of early type-setting systems.
### 1.6.9   Function Decorators

Python provides special syntax to apply higher-order functions as part of executing a def statement, called a decorator. Perhaps the most common example is a trace.
```PYTHON
>>> def trace(fn):
        def wrapped(x):
            print('-> ', fn, '(', x, ')')
            return fn(x)
        return wrapped

>>> @trace
    def triple(x):
        return 3 * x

>>> triple(12)
->  <function triple at 0x102a39848> ( 12 )
36
```

In this example, A higher-order function trace is defined, which returns a function that precedes a call to its argument with a print statement that outputs the argument. The def statement for triple has an annotation, @trace, which affects the execution rule for def. As usual, the function triple is created. However, the name triple is not bound to this function. Instead, the name triple is bound to the returned function value of calling trace on the newly defined triple function. In code, this decorator is equivalent to:
```PYTHON
>>> def triple(x):
        return 3 * x

>>> triple = trace(triple)
```

In the projects associated with this text, decorators are used for ==[[tracing]]==, as well as ==[[selecting which functions to call when a program is run from the command line]]==.
## ch1.7
### 1.7.1   The Anatomy of Recursive Functions
A common pattern can be found in the body of many recursive functions. The body begins with a ==_base case_==, a conditional statement that defines the behavior of the function for the inputs that are simplest to process. The base cases are then followed by one or more ==_recursive calls_==.
- The iterative function constructs the result from the base case of 1 to the final total by successively multiplying in each term. 
- The recursive function, on the other hand, constructs the result directly from the final term, n, and the result of the simpler problem, fact(n-1).
 we should not care about how fact(n-1) is implemented in the body of fact; we should simply trust that it computes the factorial of n-1. Treating a recursive call as a functional abstraction has been called a ==_recursive leap of faith_.==
 递归可以减少变量的数量，本身就可以传递一个变量如：
 ```python
 def even(n):
    return 1 + hailstone(n//2) 

def odd(n):
    if n==1:
        return 1
    else:
        return 1 + hailstone(3*n+1)
 ```
### hw03_7
 因为要求我们不能给一个fact名字,那就用一个lambda来代替,接收一个函数和一个参数
 ```python
return (lambda f:lambda k:f(f,k))(lambda f,k:1 if k==1 else mul(k,f(f,sub(k,1))))
```
### lab03
```python
>>> s = [7//3, 5, [4, 0, 1], 2]
>>> s[2] + [3 + 2]  
______[4, 0, 1, 5]  
>>> 5 in s[2]  
______False  
>>> s[2] * 2  
______[4, 0, 1, 4, 0, 1]
```
### Lecture: List comprehension
```python
def divisor(n):
    return [1] + [x for x in range(2,n) if n%x == 0]
```
### ch2.1
A chapter on [native data types](http://getpython3.com/diveintopython3/native-datatypes.html) in the online book Dive Into Python 3 gives a pragmatic overview of all Python's ==native data types== and how to manipulate them, including numerous usage examples and practical tips.
### 如下为 tree 和linked list（花费时间理解的较复杂的结构）的分别实现

> 4 + 2
> 4 + 1 + 1
> 3 + 3
> 3 + 2 + 1
> 3 + 1 + 1 + 1
> 2 + 2 + 2
> 2 + 2 + 1 + 1
> 2 + 1 + 1 + 1 + 1
> 1 + 1 + 1 + 1 + 1 + 1
### 2.3.6   Trees
```python
>>> def tree(root_label, branches=[]):
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [root_label] + list(branches)
        
>>> def label(tree):
        return tree[0]
        
>>> def is_leaf(tree):
        return not branches(tree)

>>> def branches(tree):
        return tree[1:]
        
>>> def partition_tree(n, m):
        """Return a partition tree of n using parts of up to m."""
        if n == 0:
            return tree(True)
        elif n < 0 or m == 0:
            return tree(False)
        else:
            left = partition_tree(n-m, m)
            right = partition_tree(n, m-1)
            return tree(m, [left, right])
            
>>> def print_parts(tree, partition=[]):
        if is_leaf(tree):
            if label(tree):
                print(' + '.join(partition))
        else:
            left, right = branches(tree)
            m = str(label(tree))
            print_parts(left, partition + [m])
            print_parts(right, partition)

>>> print_parts(partition_tree(6, 4))
4 + 2
4 + 1 + 1
3 + 3
3 + 2 + 1
3 + 1 + 1 + 1
2 + 2 + 2
2 + 2 + 1 + 1
2 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1
```
### 2.3.7   Linked Lists
```python
>>> def extend_link(s, t):
        """Return a list with the elements of s followed by those of t."""
        assert is_link(s) and is_link(t)
        if s == empty:
            return t
        else:
            return link(first(s), extend_link(rest(s), t))
            
>>> def link(first, rest):
        """Construct a linked list from its first element and the rest."""
        assert is_link(rest), "rest must be a linked list."
        return [first, rest]
        
>>> def apply_to_all_link(f, s):
        """Apply f to each element of s."""
        assert is_link(s)
        if s == empty:
            return s
        else:
            return link(f(first(s)), apply_to_all_link(f, rest(s)))
            
>>> def partitions(n, m):
        """Return a linked list of partitions of n using parts of up to m.
        Each partition is represented as a linked list.
        """
        if n == 0:
            return link(empty, empty) # A list containing the empty partition
        elif n < 0 or m == 0:
            return empty
        else:
            using_m = partitions(n-m, m)
            with_m = apply_to_all_link(lambda s: link(m, s), using_m)
            without_m = partitions(n, m-1)
            return extend_link(with_m, without_m)
            
>>> def print_partitions(n, m):
        lists = partitions(n, m)
        strings = apply_to_all_link(lambda s: join_link(s, " + "), lists)
        print(join_link(strings, "\n"))

>>> print_partitions(6, 4)
4 + 2
4 + 1 + 1
3 + 3
3 + 2 + 1
3 + 1 + 1 + 1
2 + 2 + 2
2 + 2 + 1 + 1
2 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1
```
### disc04
奇妙的python语法
```python
def sums(n, m):
    """Return lists that sum to n containing positive numbers up to m that
    have no adjacent repeats.
    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if n < 0:
        return []
    if n == 0:
        sums_to_zero = []     # The only way to sum to zero using positives
        return [sums_to_zero] # Return a list of all the ways to sum to zero
    result = []
    for k in range(1, m + 1):
        result = result + 
        [[k] + rest for rest in sums(n-k,m) if rest == [] or rest[0]!= k]
        """特指上方四行语句"""
    return result
    """只有当满足条件才会创造新的列表元素，可以等价为下面的for循环
    result_list = []
    for rest in sums(n-k, m):
        if rest == [] or rest[0] != k:  # 条件判断
           result_list.append([k] + rest)
    """
```
### Lecture : Containers
#### Strings
```python
>>> exec('curry = lambda f:lambda x:lambda y:f(x,y)')
>>> curry
<function <lambda> at 0x000002000b0434c0>
>>> from operator import add
>>> curry(add)(3)(4)
7
>>>"""claims,counts.
import this"""
'claims,counts.\nimport this'
```
#### Processing container values
```python
>>>max(range(5))
4
>>>max(0,1,2,3,4)
4
>>>max(range(5),key = lambda x:7 - (x-2)*(x-4))
3
'''
意思是在0到4范围下x取3时，右侧的key function取最大值'''
>>>sum([2,3,4])
9
>>>sum([2,3,4],5)
14
>>>sum(['2','3','4'])
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""sum(iterable[,start])返回一个值，从start开始数值叠加，default 0
但是不能处理字符串"""
>>>word = ['a','a','b']
>>>result = "".join(word) #以空字符串作为间隔
```

#### Dictionary
```python
def index(keys,values,match):
    """
    >>>index([7,9,11],range(30,50),lambda k ,v:v % k==0)
    {7: [35,42,49], 9:[36,45], 11:[33,44]}
    """
    return {k:[v for v in values if match(k,v)] for k in keys}
>>>{x * x: x for x in [1,2,3,4,5] if x > 2}
{9:3, 16:4, 25:5}
```

### Project: Cats
在problem 7卡住了，不知道每一步应该使用三种操作中哪一种才能以最少步骤实现转换。其实，既然不知道哪一种最快，那就每一次分别进行三种操作，最后min(add, remove, substitute)即可。
```python
def minimum_mewtations(typed, source, limit):

    """A diff function for autocorrect that computes the edit distance from TYPED to SOURCE.
    This function takes in a string TYPED, a string SOURCE, and a number LIMIT.
    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of edits
    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    if limit ==-1:return 1
    if source ==""or typed =="":
        return  max(len(source),len(typed))
    elif source[0]==typed[0]:
        return minimum_mewtations(typed[1:],source[1:],limit)
    else:
        add = minimum_mewtations(typed,source[1:],limit-1)
        remove = minimum_mewtations(typed[1:],source,limit-1)
        substitute = minimum_mewtations(typed[1:],source[1:],limit-1)
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 1+min(add,remove,substitute)
        # END
```
### 4.2.1   Iterators
- `Calling iter on an iterator will return that iterator, not a copy.`这样我们就可以不用考虑调用的对象是容器还是迭代器了。
### 4.2.10 Stream
- 类似链表，但是惰性计算
- ```python
  class Stream:
        """A lazily computed linked list."""
        class empty:
            def __repr__(self):
                return 'Stream.empty'
        empty = empty()
        def __init__(self, first, compute_rest=lambda: empty):
            assert callable(compute_rest), 'compute_rest must be callable.'
            self.first = first
            self._compute_rest = compute_rest
        @property
        def rest(self):
            """Return the rest of the stream, computing it if necessary."""
            if self._compute_rest is not None:
                self._rest = self._compute_rest()
                self._compute_rest = None
            return self._rest
        def __repr__(self):
            return 'Stream({0}, <...>)'.format(repr(self.first))
  ```
-  创建了一个实例`empty`就相当于链表末尾的`None`，但是又可以区分于`None`。
    
- `self._compute_rest` `self._rest`这种下划线是广泛遵守的编程规定，意思是这是作为内部变量用于内部细节的实现，区分于外部用户调用时使用的公共接口。这里如果没有下划线，调用 `rest` 时就会不断调用自己陷入无限递归。
- `self._compute_rest = compute_rest`这里是将函数对象赋予实例属性，而`self._rest = self._compute_rest()`是调用了这个函数对象将返回值赋予实例属性。
#### 装饰器
- `@property`对于紧跟在后面定义的函数创建的是一个只读的属性。当你访问这个“属性”时，你不需要加括号 ()，就像访问一个普通的变量一样，但实际上 Python 会自动替你执行它下面的那个函数，并返回函数的结果。这样显然比加上（）更像是一个属性。
- ```python
  class SafeCircle:
    def __init__(self, radius):
        # 将 radius 变成一个属性，以便在创建时就进行检查
        self.radius = radius

    @property
    def radius(self):
        """这是 'getter'，用于获取值"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """这是 'setter'，在赋值时调用，用于检查值的合法性"""
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        print(f"--- Setter 被调用，将半径设置为 {value} ---")
        self._radius = value 

    c_safe = SafeCircle(10) # <-- Setter 在这里被第一次调用

    c_safe.radius = 20 # <-- Setter 再次被调用
  ```
- `@rest.setter`（rest是函数名也就是属性名）使用这个装饰器就可以在外部对属性直接进行赋值。
#### 字符串表示形式
- `str()`用户友好，易读
- `repr()`开发者友好，精确，用于调试
- 调用 `print()` 时会首先尝试寻找并调用该对象的`__str__()`方法，如果没有就回退，寻找并调用该对象的`__repr__()`方法
- 在python的交互式环境 (>>>)中相反，总是调用`__repr__()` 来显示结果。

