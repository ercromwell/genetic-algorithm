#!/usr/local/bin/python

class ExpressionTree:
    ##'Identifiers for operator, variable'

    BINARY_LIST = ["+", "-", "*", "/", "pow"] #represents add, minus, times, divide, and powers of 2
    #UNARY = ["-"]  # add back in later if necessary
    VARIABLES = ['x']


    # constructs a default tree
    def __init__(self):
        self.root = None

    # construct a tree for a given expression, in post-traversal order
    # expression is a list for the expression
    def __init__(self, expressionList):
        self.root = self.builder(expressionList)

    #build the appropriate expression tree.
    #expression is a list
    def builder(self, expressionList):
        expStack = []

        for item in expressionList:

            if item in self.BINARY_LIST:
                rightNode = expStack.pop()
                leftNode = expStack.pop()
                temp = self.TreeNode(item, leftNode, rightNode)
                expStack.append(temp)
            ## elif item in self.UNARY: # add back in later if necessary
            ##     leftNode = expStack.pop()
            ##     rightNode = null
            ##     temp = self.TreeNode(item, leftNode, rightNode)
            ##     expStack.append(temp)
            else:
                temp = self.TreeNode(item, None, None)
                expStack.append(temp)

        return expStack.pop()


    #creates random expressionLists
    def expressionListGenerator(size)
        expList = []
        x = 0
        while (x < size)
            r = random.choice(float in range (0, 100))
            if (r < 45): #choose random operation 45% of time
                expList.append(random.choice(BINARY_LIST))
            elif (r < 55): #choose random variable 10% of time
                expList.append(random.choice(VARIABLES))
            else: #choose random constant 45% of time
                expList.append(random.choice(int in range (-10, 10)))
            x += 1
        return expList
                
    #prints expression tree in correct order
    def printTree(self):
        string = ""
        print self.printTreeHelper(self.root, string )
        
    def printTreeHelper(self,node, string):

        #base case
        if(node is None):
            return ""

        #recursive case
        string1 = "(" + self.printTreeHelper(node.left, string) # print left subtree

        string2 = self.printTreeHelper(node.right, string) + ")" # print right subtree

        s = ''
        if node.value == 'pow':
            s = '^'
        else:
            s = node.value
            
        return string1 + s + string2


    #calultes expression value for input i, for functions of one variable 'x'
    # i is a float/double
    def calculate(self, i):
        return self.calculateHelper(self.root, i)

    def calculateHelper(self, node, i):

        #base case, reached a constant node, or variable node
        if node is None:
            return 0

        #recursive case
        leftValue = self.calculateHelper(node.left, i)
        rightValue = self.calculateHelper(node.right, i)

        value = 0
        
        #node is operator value
        if node.value in self.BINARY_LIST:

            #operator is '+'
            if node.value == '+':
                value = leftValue + rightValue

            #operator is '-'
            if node.value == '-':
                value = leftValue - rightValue

            #operator is '*'
            if node.value == '*':
                value = leftValue * rightValue 

            #operator is '/', check if divide by zero
            if node.value == '/':

                #check if divide by 0, then do division
                if rightValue == 0:
                    value =  1    # hack, return extremely large number
                    print "ERROR: trying to divide by 0"
                else:
                    value = leftValue / rightValue 

            #operator is 'pow'
            if node.value == 'pow':
                value = pow(leftValue, rightValue)

        #node is constant or variable
        else:
            if node.value == 'x':
                value = i
            else:
                value = float(node.value)
    
        return value

    #calultes expression value for input i1, 12, 13, for functions of three variable 'x1', 'x2', 'x3'
    # i is a float/double
    def calculateThree(self, i1, i2, i3):
        return self.calculateThreeHelper(self.root,  i1, i2, i3)

    def calculateThreeHelper(self, node, i1, i2, i3):

        #base case, reached a constant node, or variable node
        if node is None:
            return 0

        #recursive case
        leftValue = self.calculateThreeHelper(node.left,  i1, i2, i3)
        rightValue = self.calculateThreeHelper(node.right,  i1, i2, i3)

        value = 0
        
        #node is operator value
        if node.value in self.BINARY_LIST:

            #operator is '+'
            if node.value == '+':
                value = leftValue + rightValue

            #operator is '-'
            if node.value == '-':
                value = leftValue - rightValue

            #operator is '*'
            if node.value == '*':
                value = leftValue * rightValue 

            #operator is '/', check if divide by zero
            if node.value == '/':

                #check if divide by 0, then do division
                if rightValue == 0:
                    value =  1   # hack, return extremely large number
                    print "ERROR: trying to divide by 0"
                else:
                    value = leftValue / rightValue 

            #operator is 'pow'
            if node.value == 'pow':
                value = pow(leftValue, rightValue)

        #node is constant or variable
        else:
            if node.value == 'x1':
                value = i1*1.0
            elif  node.value == 'x2':
                value = i2*1.0
            elif  node.value == 'x3':
                value = i3*1.0
            else:
                value = float(node.value)*1.0
    
        return value
 
    #returns copy of the tree
    def copyTree(self):
        copy_root = self.copyHelper(self.root)
        copy_tree = ExpressionTree(['a'])
        copy_tree.root  = copy_root
 
        return copy_tree

    def copyHelper(self, node):

        #base case: reach empty node
        if node is None:
            return None

        #recursive case
        left_node = self.copyHelper(node.left)
        right_node = self.copyHelper(node.right)

        new_node = self.TreeNode(node.value, left_node, right_node)

        return new_node

    #This class represents a node in our expression tree
    class TreeNode:

        #construct a new node with a specified value
        # left and right are TreeNodes as well
        def __init__(self, value, left, right): ##for making constructor
            self.value = value  #data field
            self.left = left    # pointer to left subtree
            self.right = right  # pointer to right subtree

    ##########

