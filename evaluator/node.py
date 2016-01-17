import operator

class Node:
    """ Node class implements behavior of a Node in the binary tree used to
    evaluate mathematical expressions; this tree is created from parse.into_binary_tree """

    def __init__(self, type, value, left=None, right=None):
        self._type = type
        self._value = value
        self._left = left
        self._right = right
        self._parent = None

    def weight(self):
        """ Returns a Node's weight
        NOTE: Needs to be improved
        To manage operation precedence (order) we assign weights to each node type """
        if self.is_number():
            return 1
        types = {'(': 5, '+': 4, '-': 4, '*': 2, '/': 2}
        return types[self._value]

    def is_operator(self):
        """ Returns True if this is an operator """
        return self._type == 'operator'

    def is_number(self):
        """ Returns True if this is a number """
        return self._type == 'number'

    def reduce(self):
        """ Reduces branch to a value by combining all child branches & leafs """
        ops = {'+': operator.add, '(': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        if self.is_operator():
            op = ops[self._value]
            left_value = self._left.reduce() if self._left else 0
            right_value = self._right.reduce() if self._right else 0
            result = op(right_value, left_value)
            # if self._value == '-' and self._right is None:
            #     result = -result
            return result
        else:
            return float(self._value)

    def __iter__(self):
        """ Allow node to be iterated """
        items = []
        if self._left: items.append(self._left)
        if self._right: items.append(self._right)
        return iter(items)

    def push(self, node):
        """ Pushes a node into branch """
        if not node:
            return
        if not self._left or (self._left and not self._left.is_number() and node.weight() > self._left.weight()):
            node.push(self._left)
            self._left = node
            node._parent = self
        elif not self._right or (self._right and node.weight() > self._right.weight()):
            node.push(self._right)
            self._right = node
            node._parent = self
        else:
            if self._left and self._left.is_operator():
                self._left.push(node)
            elif self._right and self._right.is_operator():
                self._right.push(node)

    def remove(self):
        if self._parent:
            if self._parent._left is self:
                self._parent._left = None
            elif self._parent._right is self:
                self._parent._right = None

    def print(self, tab=0):
        """ Print the node structure recursively """
        print('  ' * tab, 'node type=%s, value=%s' % (self._type, self._value))
        if self._left:
            print('  ' * tab, 'left:')
            self._left.print(tab + 1)
        if self._right:
            print('  ' * tab, 'right:')
            self._right.print(tab + 1)

    def swap(self, node):
        self._left, node._left = node._left, self._left
        self._right, node._right = node._right, self._right

    def __repr__(self):
        """ Very useful for debugging """
        return '%s %s' % (self._type, self._value)

