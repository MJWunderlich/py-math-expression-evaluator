# This script exemplifies how to use evaluator.expression to evaluate
# arbitrary mathematical expressions with the same accuracy as native
# computations.
#
# evaluator.expression uses a binary (red-black) tree to process mathematical
# expressions of varying degrees of complexity - it supports operator precedence,
# parenthesized groups, and can use variables, provided that a dict for variable
# lookup is provided.
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
#     y    x   -0.5   pi2

result = evaluator.expression(expr, local_data=locals())
evaled = eval(expr)

title = 'ME*3: (Mathematical Expression Evaluation Example)'

print()
print(title)
print('–'*len(title))
print('expression: ', expr)
print('–'*len(title))
print('evaluator.expression() result: ', result)
print('eval() result                : ', evaled)
