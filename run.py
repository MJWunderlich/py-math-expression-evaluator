# This script exemplifies how to use evaluator.expression to evaluate
# arbitrary mathematical expressions with the same accuracy as native
# computations.
#
# evaluator.expression uses a binary (red-black) tree to process mathematical
# expressions of varying degrees of complexity - it supports operator precedence,
# parenthesized groups, and can use variables, provided that a dict for variable
# lookup is given.
#
# In the binary tree, branches represent operators, and leafs are the operands.
# Variables are looked-up during parsing stage, so the tree only sees numerical
# values.
#
# Expressions are read right-to-left, even though the tree is left aligned. The
# tree is traversed depth-first, each branch combining it's leafs using it's
# designated math operator.
#
# This example is a quick rough-draft and still needs to be improved.

import evaluator
import math

pi = math.pi
pi2 = pi/2

expr = "(4 / 59) * 2 + (-0.5 / pi2) * pi"

# The above expressions binary-tree representation:
#
#                  +
#               /     \
#             "*"     "*"
#            /  \     /  \
#          "("   2  "("   pi
#         /         /
#       "/"       "/"
#      /  \      /   \
#     4   59   -0.5   pi2

# evaluator.expression supports variables -- provided a dict for variable lookup is given
# functions & callables are not yet supported
result = evaluator.expression(expr, local_data=locals())

# also compute using eval() to test accuracy
evaled = eval(expr)

title = 'ME*3: (Mathematical Expression Evaluation Example)'

print()
print(title)
print('–' * len(title))
print('expression: ', expr)
print('–' * len(title))
print('evaluator.expression() result: ', result)
print('eval() result                : ', evaled)
