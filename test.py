from ExpressionTree import ExpressionTree
import random
import GeneticAlgorithm


list = ['3', '7', '*', 'x', '+']
l2 = [ 'a', 'b', '/', 'c', '-']


print list

tree = ExpressionTree(list)
tree2 = ExpressionTree(l2)
print '1st parent'
tree.printTree()
print '2nd parent'
tree2.printTree()

child1, child2 = GeneticAlgorithm.crossParents(tree, tree2, 1)

print '1st child'
child1.printTree()
print '2nd childe'
child2.printTree()

## copy = tree.copyTree()
## node, isLeft = GeneticAlgorithm.chooseSplitNode(tree, .3)

## if isLeft:
##     node.left.value = 'penis'
##     print tree.printTreeHelper(node.left, '')
## else:
##     node.right.value = 'penis'
##     print tree.printTreeHelper(node.right, '')

## print 'changed tree'
## tree.printTree()
## print 'original tree'
## copy.printTree()
