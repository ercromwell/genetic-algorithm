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
num_gen = 3
pop_size = 500
num_vars = 1
stop_prob = 0.8 #for stopping to split a tree
init_depth = 4 #max initial depth for random trees

GeneticAlgorithm.run_symbolic_regression(filename, num_gen, pop_size, num_vars, stop_prob, init_depth)




