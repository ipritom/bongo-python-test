class Node:
    def __init__(self,value,parent=None):
        self.value = value
        self.parent = parent


def lca(node1, node2):
    '''
    Input: lca(node1,node2)
    Return: Least Common Ancestor

    Runtime: O(n)
    Memory: O(n)
    '''
    #raise TypeError
    if isinstance(node1,Node)==False or isinstance(node2,Node)==False:
        raise TypeError("Input data must be 2 nodes of a tree")


    root_count = [] #for detecting "More than One Tree"
    
    ###lca algorithm
    if node1.value == node2.value:
        return node1.value
        
    #tracking lraversed nodes value
    node1_exp= [node1.value]
    node2_exp = [node2.value]

    while True:
        if node1.parent==None:root_count.append(node1)
        if node2.parent==None:root_count.append(node2)
        if len(root_count)>1:
            raise Exception("More than One Tree Detected")
        if node1.parent:
            #go to parent node
            node1 = node1.parent
            if node1.value in node2_exp:
                return node1.value
            node1_exp.append(node1.value)

        if node2.parent:
            #go to parent node
            node2 = node2.parent
            if node2.value in node1_exp:
                return node2.value
            node2_exp.append(node2.value)



            
if __name__ == '__main__':
    #creating tree
    node1 = Node(1)
    node2 = Node(2,node1)
    node3 = Node(3,node1)
    node4 = Node(4,node2)
    node5 = Node(5,node2)
    node6 = Node(6,node3)
    node7 = Node(7,node3)
    node8 = Node(8,node4)
    node9 = Node(9,node4)

    print(lca(node6,node7)) #ans 3

    print(lca(node9,node4)) #ans 4

    print(lca(node8,node7)) #ans 1

