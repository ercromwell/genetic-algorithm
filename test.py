from ExpressionTree import ExpressionTree
import random
import GeneticAlgorithm


##list = ['3', '7', '*', 'x', '+']
## l2 = [ 'a', 'b', '/', 'c', '-']


## print list

## tree = ExpressionTree(list)
## tree2 = ExpressionTree(l2)
## print '1st parent'
## tree.printTree()
## print '2nd parent'
## tree2.printTree()

filename = 'data.txt'

#filename = 'generator1_output.txt'

data = GeneticAlgorithm.organizeData(filename)

random.shuffle(data) #shuffle data

train_test_split = int(len(data) * 0.8)

print train_test_split

training_set = data[:train_test_split]
test_set = data[train_test_split:]


l2 = [ 'x1', 'x2', '/', 'x3', '-']
tree = ExpressionTree(l2)

train_fitness = GeneticAlgorithm.calculateFitness([tree], data, 3)

print train_fitness


