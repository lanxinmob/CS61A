# scheme interpreter
## part 1
### pro5
- `quote`（或`'`）的作用是阻止求值，把代码当数据返回
- 在 `scheme_forms.py` 中实现 `do_quote_form `函数，你只需要返回 `quote` 表达式的第一个（也是唯一一个）操作数，而无需对其进行任何求值。
-  因为对这样一个表达式 `(quote (a b c))` ，`expressions` 就是 `((a b c))`，目标是返回未被求值的操作数 `(a b c)`,所以返回 `expressions.first`就行。

## pro9
- lambda 的 frame 是紧跟着他自己的 procedure 的，所以不只是简单的当前调用时的环境 env ，这样使用的是全局的 global frame ，而要使用定义时的环境基础上创建的 frame。
- procedure.env 是他自己的定义时环境，不会出现新 bind 了但是还是使用原来的 binding 的情况，实现真正的词法作用域，使闭包正常工作。

## pro15
### cons  list 的本质区别
- `(cons 3 4)` ; → (3 . 4)
- 它创建一个 Pair，第一个元素是 3，第二个是 4。4 不是一个列表，所以结果是一个 dotted pair。
- `Pair(3, 4)  # not a list, just a pair`
- `(list 3 4)` ; → (3 4)
- 它创建了一个链式结构：`(cons 3 (cons 4 nil))`。每个元素被包在一个 `Pair` 中，第二个 `Pair` 的 .rest 是 nil
- `Pair(3, Pair(4, nil))`，这是一个 真正的 Scheme list。
- `cons` 是原始的构造函数，它生成一个 `pair`（可以是 `list` 的一部分，也可以不是）；而 `list` 是用多个 `cons` 组成的，每次 `cons` 的 `.rest` 都是一个 `list`（或者是 nil），从而形成链表结构。