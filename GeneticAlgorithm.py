from ExpressionTree import ExpressionTree
import random

#1: Generate random expression Trees
def generateTrees(size):
    treeArray = []
    for x in range (0, 1000):
       lst = expressionListGenerator(size)
       treeArray.append(ExpressionTree(lst))
    return treeArray

#2: Calculate fitness function for each tree
def calculateFitness(treeArray):
    fitnessArray = []
    data = open(SOMETHING.txt)
    for tree in treeArray:
        fitness = 0
        for line in data:
            if lineNumber % 5 != 0: #skip over every 5th line to use at the end
                for entry in txtFile
                x = scanner.next()
                fitness += (tree(x) - scanner.next())^2
        fitnessArray.append(fitness)
        close(SOMETHING.txt)
    return fitnessArray

#Calculate error of function on f(x)= y, where x is input and y is actual value, for one variable
#expTree is expression tree, x is input, y is actual function value
def errorOne(expTree, x, y):
    y_approx = expTree.calculate(x)
    error = abs(y_approx - y)

    return pow(error, 2)

#calculates least squares of a given function expTree to measure fit
# data is the 2D array of inputs, where data[i][0] = input,  data[i][1] = correct ouput 
def leastSquaresOne(expTree, data):
    least_square = 0
    for points in data:
        input = points[0]
        least_square+= errorOne(expTree, input, points[1])

    return least_square

#3: Select trees to breed, cross over, create children


#post: create two children trees from parents expTree1, expTree2
#stop_prob = proability stop at a given subtree
def crossParents(expTree1, expTree2, stop_prob):
    child1 = expTree1.copyTree() #copy of expTree1, need to make copy method
    child2 = expTree2.copyTree() #copy of expTree2
        
    isLeft1 = False #whether to use left subtrree of node for split, for child1
    isLeft2 = False #whether to use left subtree of node for split, for child2

    #choose place to split expTree1
    splitNode1, isLeft1 = chooseSplitNode(child1, stop_prob)
   #choose place to split expTree2
    splitNode2, isLeft2 = chooseSplitNode(child2, stop_prob)

    
    #cross over, make babies
    #splitting on left subtrees for both, do I need copy of nodes????? mutable pointers?????
    if isLeft1 and isLeft2:
        temp1 = splitNode1.left
        temp2 = splitNode2.left
        splitNode1.left = temp2
        splitNode2.left = temp1
        
    #splitting on left subtree for 1st expression, right for the other
    if isLeft1 and (not isLeft2):
        temp1 = splitNode1.left
        temp2 = splitNode2.right
        splitNode1.left = temp2
        splitNode2.right = temp1

    #splitting on right subtree for 1st expression, left for the other
    if not isLeft1 and isLeft2:
        temp1 = splitNode1.right
        temp2 = splitNode2.left
        splitNode1.right = temp2
        splitNode2.left = temp1

    #splitting on right subtrees for both, 
    if not isLeft1 and not isLeft2:
        temp1 = splitNode1.right
        temp2 = splitNode2.right
        splitNode1.right = temp2
        splitNode2.right = temp1
    
    return child1, child2


# choose subtree to swap for expTree, double check to make sure it is mutable
def chooseSplitNode(expTree, stop_prob):
    node = expTree.root
    prev_node = None # used to keep track of previous node, in case hit terminal node
    isLeft = False

    found_subtree = False

    #search for place to split expTree
    while not found_subtree:

        #check if node is leaf node
        if node.left is None and node.right is None:
            node = prev_node
            break
        
        choice = random.random()
        #go to left subtree, if choice < 0.5
        if choice <= 0.5:
            isLeft = True
        #go to right subtree, if choice > .5
        else:
            isLeft = False

        choose_node = random.random()
        #stop searching, use appropriate subtree
        if choose_node <= stop_prob:
            found_subtree = True
        #keep looking for split node, according to appropriate subtree
        else:
            prev_node = node
            if isLeft:
                node = node.left
            else:
                node = node.right

    return node, isLeft



#4: Mutation for select trees
def mutate(expTree):
    #mutate 1% of trees by picking 1 in 100
    i = random.choice(int in range (0, 100))
    x = 0
    while (x < expTree.length)
        if (x = i % 100):

            #choose random node in(expTree[x]) !!!!!!!!!!
            
            if (node.value is in BINARY_LIST) #switch operation if it's an operation
                node.value = random.choice(BINARY_LIST)
            elif (node.value is int) #switch integer if it's an int
                node.value = random.choice(int in range (-10,10))
            elif (node.value is in VARIABLE_LIST): #switch variable if it's a variable
                node.value = random.choice(VARIABLE_LIST)
        x += 1
