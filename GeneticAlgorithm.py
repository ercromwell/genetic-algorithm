from ExpressionTree import ExpressionTree
import random

# run genetic algorithm to solve for correct function of given data in 'filename'
# 'num_gen' = number of generations, 'num_vars' = number of variables in the function
# 'pop_size' = sze of the population
def run_symbolic_regression(filename, num_gen, pop_size, num_vars):

    #import data from filename
    data = organizeData(filename)

    #divide data into training/test set
    random.shuffle(data) #shuffle data

    train_test_split = int(len(data) * 0.8)

    training_set = data[:train_test_split]
    test_set = data[train_test_split:]
    
    #generate random trees
    parent_trees = generateTrees(pop_size, 2)
    print len(parent_trees)
    for tree in parent_trees:
        tree.printTree()
    
    #calculate fitness of parents
    fitness = calculateFitness(parent_trees, training_set, num_vars)
    print len(fitness)

    for gen in range(0, num_gen):
        print gen
        #check if found correct function, has 0 fitness
        best = sorted( zip( fitness, parent_trees) )
        
        if best[0][0] == 0:
            print 'Exact solution is: '
            best[0][1].printTree()
        

        #otherwise, keep searching
        max_fitness = [ 1/x for x in fitness]
        sum_fit = sum(fitness)

        #normalize fitness scores
        norm_fitness = [ x/sum_fit for x in max_fitness]

        #set up probability sections
        prob_intervals = []
        prob_intervals.append(norm_fitness[0])
        for i in range(1, len(norm_fitness)):
            prob_intervals.append( norm_fitness[i] + prob_intervals[i-1] )

        children_trees = []
        # make children trees
        for i in range(0, pop_size-1):
        #select parents, ensure are not the same
            int1 = random.randint(0, pop_size-1)
            int2 = random.randint(0, pop_size-1)
            while(int1 == int2):
                int2 = random.randint(0, pop_size-1)

            parent_1 = parent_trees[int1]
            parent_2 = parent_trees[int2]

            child_1, child_2 = crossParents(parent_1, parent_2, 0.7)

            children_trees.append(child_1)
            children_trees.append(child_2)

        #OPTIONS: keep only children_trees, make the new OR mix with parents, keep top parents and childre

        children_fitness = calculateFitness(children_trees, training_set, num_vars)
         
        #OPTION 1: KEEP ONLY CHILDREN_TREE
        top_children = sorted( zip(children_fitness, children_trees) )

        parent_trees = []
        fitness = []
        for (score, tree) in top_children[:pop_size]:
            parent_tree.append(tree)
            fitness.append(score)

        ## #OPTION 2: MIX PARENTS AND CHILDREN
        ## labeled_both = []

        ## for n in range(0, pop_size):
        ##     labeled_both.append( (children_fitness[n], children_trees[n]) )
        ##     labeled_both.append( (fitness[n],  parent_trees[n]) )

        ## parent_trees = []
        ## fitness = []

        ## for (f, tree) in sorted(labeled_both)[:pop_size]:
        ##     parent_trees.append(tree)
        ##     fitness.append(f)
    

    #choose best tree, based on test set
    final_fitness = calculateFitness(parent_trees, test_set, num_vars)

    best_pair = sorted( zip(final_fitness, parent_trees) )[:1]

    best_tree = best_pair[1]
    print 'The function is most likely: '
    best_tree[1].printTree()
    
    


#0: get data from file 'fiilename". Can be used for 3 variable or one variable functions
def organizeData(filename):
    data = []
    data_file = open(filename)

    for line in data_file:
        data_values = line.split()

        numbers = [] # list that holds input and outputs
        for v in data_values:
            numbers.append(float(v))

        data.append(numbers)

    data_file.close()
    
    return data

#1: Generate random expression Trees
def generateTrees(pop_size, max_depth):
    treeArray = []
    dummyTree = ExpressionTree(['1'])
    for x in range (0, pop_size):
       tree = dummyTree.treeGenerator(max_depth)
       treeArray.append(tree)
    return treeArray

#2: Calculate fitness function for each tree, lets assume we have already opened, loaded data, so we dont have to keep doing
## it over again. num_var = number of variables in the function
def calculateFitness(treeArray, data, num_var):
    fitnessArray = []
    for tree in treeArray:
        fitness = 0

        for data_points in data:
            if num_var == 1:
                x = data_points[0]
                y = data_points[1]
                fitness+= pow( tree.calculate(x) - y, 2)
            if num_var == 3:
                x1 = data_points[0]
                x2 = data_points[1]
                x3 = data_points[2]
                y = data_points[3]
                fitness+= pow( tree.calculateThree(x1, x2, x3) - y, 2) 

        fitnessArray.append(fitness)
        
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

#4: Mutation for select trees, needs editing for variable list
def mutate(expTreeArray):
    #mutate 1% of trees by picking 1 in 100
    i = random.choice(int in range (0, 100))
    x = 0
    while (x < expTree.length):
        if (x % 100 == i):

            node, isLeft = chooseSplitNode(expTreeArray[x], 0.5)
            
            if (node.value in BINARY_LIST): #switch operation if it's an operation
                node.value = random.choice(BINARY_LIST)
            elif (node.value in VARIABLE_LIST): #switch variable if it's a variable
                node.value = random.choice(VARIABLE_LIST)
            else: #switch integer if it's an int
                node.value = ''+ random.choice(int in range (-10,10))
        x += 1

