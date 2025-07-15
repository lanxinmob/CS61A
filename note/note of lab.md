## Lab5 Mutability,Iterators
- `append(elem)`: Add elem to the end of the list. but **!!!Return None!!!**
- `extend(s)`: Add all elements of iterable s to the end of the list.but **!!!Return None!!!**
- `insert(i, elem)`: Insert elem at index i. If i is greater than or equal to the length of the list, then elem is inserted at the end. This does not replace any existing elements, but only adds the new element elem. **!!!Return None.!!!**
- `remove(elem)`: Remove the first occurrence of elem in list. **!!!Return None!!!**. Errors if elem is not in the list.
- `pop(i)`: Remove and return the element at index i.
- `pop()`: Remove and return the last element.
### for & while
- `for i in range(len(s))`
  - `range(len(s))` 这部分只在循环开始前计算一次
- `while index < len(s)`
这个条件判断在每一次循环开始前都会重新计算 `len(s)`。 