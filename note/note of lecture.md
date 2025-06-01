### Lecture7.Function Examples
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