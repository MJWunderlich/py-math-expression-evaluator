import re
import collections

# Local imports
from .node import Node


def parse_expression(expr, local_data=None):
    """ Parses a math expression into a list """
    i = 0
    data = []
    while True:
        if i >= len(expr):
            break

        if expr[i] == ' ':
            i += 1
        elif re.search(r'^[\d,.]+', expr[i:]):
            number = []
            while re.search('^-?[\d,.]+', expr[i:]):
                number.append(expr[i])
                i += 1
            data.append({'type': 'number', 'value': ''.join(number)})
        elif re.search(r'^[_\w][_\w\d]*', expr[i:]):
            # If we find any identifier starting with _ or [a-zA-Z] then this is a variable
            # We will attempt to get it's value from the variables dictionary (local_data)
            # This local_data will usually be set to locals() or a defaultdict that returns 0
            number = []
            while re.search(r'^[_\w][_\w\d]*', expr[i:]):
                number.append(expr[i])
                i += 1
            # Grab value from local_data and append as a number
            # Functions are not allowed
            variable_name = ''.join(number)
            if not local_data or variable_name not in local_data:
                raise Exception('Variable not defined: %s' % variable_name)
            variable = local_data[variable_name]
            try:
                variable = float(variable)
            except ValueError:
                raise Exception('Invalid variable type found for: %s, with type: %s' % (variable_name, type(variable)))
            data.append({'type': 'number', 'value': variable})
        elif re.search(r'\+|\-|/', expr[i]):
            data.append({'type': 'operator', 'value': expr[i]})
            i += 1
        elif expr[i] == ')':
            data.append({'type': 'operator', 'value': '('})
            i += 1
        elif expr[i] == '(':
            data.append({'type': 'end', 'value': ')'})
            i += 1
        elif expr[i] == '*':
            if i + 1 < len(expr) and expr[i + 1] == '*':
                data.append({'type': 'operator', 'value': '**'})
                i += 2
            else:
                data.append({'type': 'operator', 'value': '*'})
                i += 1
        else:
            raise Exception('Character is not an operator or a number: ', expr[i])

    return [x for x in reversed(data)]


def into_binary_tree(items):
    stack = collections.deque()
    last_number = None
    last_operator = None
    for i in range(len(items)):
        node = Node(**items[i])
        if node.is_operator():
            if last_number:
                node.push(last_number)
                last_number = None
            if last_operator:
                node.push(last_operator)
                last_operator = None
            if stack:
                stack[0].push(node)
            stack.appendleft(node)
        if node._value == ')':
            if last_number:
                stack[0].push(last_number)
                last_number = None
            while stack[0]._value != '(':
                stack.popleft()
            if len(stack) == 1:
                last_operator = stack[0]
            stack.popleft()
            if len(stack) and stack[0]._value in '*/':
                # After poping the "()" the top of stack is a "*" or "/" operation
                # To conserve operator precedence ("*" and "/" come first), reduce these operations to numbers
                # And set them as the last_number available for consumption
                last_operator = stack.popleft()
                last_number = Node(type='number', value=last_operator.reduce())
                last_operator.remove()
                last_operator = None
        elif node.is_number():
            if last_number:
                raise Exception('Cannot have 2 consecutive numbers: ', last_number._value, ' and ', node._value)
            last_number = node
    if last_operator and stack:
        stack.appendleft(last_operator)
    if last_number:
        if stack:
            stack[-1].push(last_number)
        else:
            stack.append(last_number)
    return stack[-1]


def expression(expr, local_data, as_node=False):
    data = parse_expression(expr, local_data=local_data)
    root = into_binary_tree(data)
    if as_node:
        return root
    return root.reduce()
