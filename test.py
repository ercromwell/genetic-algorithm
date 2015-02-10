from ExpressionTree import ExpressionTree

list = ['x1', 'x3', '*', 'x2', '/']

print list

tree = ExpressionTree(list)
tree.printTree()
print tree.calculateThree(5, 0, 7) 
