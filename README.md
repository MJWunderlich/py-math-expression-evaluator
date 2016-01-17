# Math Expression Evaluator for Python

This script exemplifies how to use binary trees to process arbitrary mathematical
expressions with the same accuracy (but not speed) as native computations.

### How?

`evaluator.expression` is the main interface. It will compile a binary (red-black)
from the given expression and use it to solve expressions of varying degrees of simplicity.
It supports operator precedence (beta), parenthesized groups, and can use variables
_provided that a dict for variable lookup is given_.

In the binary tree, branches represent operators, and leafs are the operands.
Variables are looked-up during parsing stage, so the tree only sees numerical
values.

Expressions are read right-to-left, even though the tree is left aligned. The
tree is traversed depth-first, each branch combining it's leafs using it's
designated math operator.

### Example

This expression: `"(4 / 59) * 2 + (-0.5 / 1.7) * 3.14"` is compiled into this binary tree:

```
                 +
              /     \
            "*"     "*"
           /  \     /  \
         "("   2  "("   3.14
        /         /
      "/"       "/"
     /  \      /   \
    4   59   -0.5   1.7
```

As for variables, simply create a dict where variables are key:value entries and
pass it to `local_data` param when calling `evaluator.expression`, like so:

```
import math
import evaluator

# variables for our expression
pi = math.pi
pi2 = pi/2

# expression using variables, yay!
expr = "(4 / 59) * 2 + (-0.5 / pi2) * pi"

# because variables are defined in local scope, simply use locals() as our variables dict
result = evaluator.expression(expr, local_data=locals())
```

### Why?

Because Python rocks! - and I entertain myself making these contraptions :)

### Disclaimer

This example is a quick rough-draft and still needs to be improved.
