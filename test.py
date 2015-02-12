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

filename = 'generator1_output.txt'
num_gen = 5
pop_size = 30
num_vars = 1

GeneticAlgorithm.run_symbolic_regression(filename, num_gen, pop_size, num_vars)


## data = GeneticAlgorithm.organizeData(filename)

## ## random.shuffle(data) #shuffle data

## treeArray = GeneticAlgorithm.generateTrees(10)

## fitness = GeneticAlgorithm.calculateFitness(treeArray, data, 1)

## for i in range(0, len(fitness) ):
##     print "Tree is: " 
##     treeArray[i].printTree()
##     print "    Fitness is: " + str(fitness[i])


