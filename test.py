from ExpressionTree import ExpressionTree
import random
import GeneticAlgorithm


##list = ['3', '7', '*', 'x', '+']
## l2 = [ 'x1', 'x2', '/', 'x3', '-']

## l2 = ['1']
## tree = ExpressionTree(l2)

## new_tree = tree.treeGenerator(2)

## new_tree.printTree()

## filename = 'data.txt'

filename = 'generator1_data.txt'
num_gen = 40
pop_size = 500
num_vars = 1
stop_prob = 0.55 #for stopping to split a tree
init_depth = 4 #max initial depth for random trees
print "num_gen: " + str(num_gen)
print "pop_size: " + str(pop_size)
print "num_vars: " + str(num_vars)
print "stop_prob: " + str(stop_prob)
print "init_depth: " + str(init_depth)

GeneticAlgorithm.run_symbolic_regression(filename, num_gen, pop_size, num_vars, stop_prob, init_depth)




