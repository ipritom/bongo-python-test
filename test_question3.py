import unittest
from solution.question3 import *

class TestQuestion(unittest.TestCase):
    
    def test_case1(self):
        '''
        Input: 2 Nodes from a Single Tree
        '''
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

        #testing
        self.assertEqual(lca(node6,node7),3)
        self.assertEqual(lca(node9,node4),4)
        self.assertEqual(lca(node8,node7),1)


    def test_case2(self):
        '''
        Input: 2 Nodes from 2 different tree
        '''
        #creating tree 1
        node1 = Node(1)
        node2 = Node(2,node1)
        node3 = Node(3,node1)
        node4 = Node(4,node2)
        node5 = Node(5,node2)
        node6 = Node(6,node3)
        node7 = Node(7,node3)
        node8 = Node(8,node4)
        node9 = Node(9,node4)

        #creating tree 2
        node10 = Node(10)
        node11 = Node(11,node10)
        node12 = Node(12,node10)

        #testing 
        with self.assertRaises(Exception):
            lca(node7,node12)


    def test_type(self):
        #creating tree 1
        node1 = Node(1)
        node2 = Node(2,node1)
        node3 = Node(3,node1)
        node4 = Node(4,node2)
        
        #testing
        with self.assertRaises(TypeError):
            lca('string',node4)

        with self.assertRaises(TypeError):
            lca(2,4)
        
        with self.assertRaises(TypeError):
            lca(node2,Node)




if __name__=='__main__':
    unittest.main()