from ExpressionTree import ExpressionTree

list = ['x1', 'x3', '*', 'x2', '/']

print list

tree = ExpressionTree(list)
tree.printTree()
print tree.calculateThree(5, 0, 7) 


  #returns node, branch to split on (isLeft)
    def chooseSplitNode(expTree, stop_prob):

        node = expTree.root
        isLeft = False

        found_subtree = False

        #search for place to split expTree
        while !found_subtree:
            choice = random.random()
            #go to left subtree, if choice < 0.5
            if choice < 0.5:
                isLeft = True
            #go to right subtree, if choice >= .5
            else:
                isLeft = False

            choose_node = random.random()
            #stop searching, use appropriate subtree
            if choose_node <= stop_prob:
                found_subtree = True
            #keep looking for split node, according to appropriate subtree
            else:
                if isLeft:
                    node = node.left
                else:
                    node = node.right

        return node, isLeft
