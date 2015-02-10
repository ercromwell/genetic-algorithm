from ExpressionTree import ExpressionTree
import random

#0: import function data


#1: Generate random expression Trees

#2: Calculate fitness function for each tree

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
    child1 = ExpressionTree() #copy of expTree1
    child2 = ExpressionTree() #copy of expTree2
        
    leftNode1 = False #whether to use left subtrree of node for split, for child1
    leftNode2 = False #whether to use left subtree of node for split, for child2

    #####choose place to split expTree1##########
    splitNode1 = child1.root #pointer for location in expression tree
    found_subtree = False

    #search for place to split expTree1
    while !found_subtree:
    
        choice = random.random()
        #go to left subtree, if choice < 0.5
        if choice < 0.5:
            leftNode1 = True
        #go to right subtree, if choice >= .5
        else:
            leftNode1 = False

        choose_node = random.random()
        #stop searching, use appropriate subtree
        if choose_node < stop_prob:
            found_subtree = True
        #keep looking for split node, according to appropriate subtree
        else:
            if leftNode1:
                splitNode1 = splitNode1.left
            else:
                splitNode1 = splitNode1.right
        
    
   ########choose place to split expTree2#########
    splitNode2 = child2.root #pointer for location in expression tree
    found_subtree = False

    #search for place to split ExpTree2
    while !found_subtree:

        #node is terminal node
    
        choice = random.random()
        #go to left subtree, if choice < 0.5
        if choice < 0.5:
            leftNode2 = True
        #go to right subtree, if choice >= .5
        else:
            leftNode2 = False

        choose_node = random.random()
        #stop searching, use appropriate subtree
        if choose_node < stop_prob:
            found_subtree = True
        #keep looking for split node, according to appropriate subtree
        else:
            if leftNode2:
                splitNode2 = splitNode1.left
            else:
                splitNode2 = splitNode1.right

    
    #cross over, make babies
    #splitting on left subtrees
    if( leftNode1 and leftNode2)
    



    return child1, child2

#4: Mutation for select trees
