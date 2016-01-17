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

### Why?

Because Python rocks! - and I entertain myself making these contraptions :)

### Disclaimer

This example is a quick rough-draft and still needs to be improved.
