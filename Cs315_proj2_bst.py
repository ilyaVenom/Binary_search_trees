# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:44:26 2022

@author: segal
"""

# where the nil is the leaf that will point to null at the end
nil = None 
class Node:
    def __init__(self, data):
        self.data = data # maybe use data as a key 
        # ex. self.ref = None
        self.left = None
        self.right = None
        self.parent = None # the parent is the val or value 
    
        
class LinkedList: # this the tree (T) 
    def __init__(self):
        self.head = None
        
# list 1 build the file to open and :
file = open("testBad.csv", "r") # for each of the 3 files
text = file.readlines()
# may remove pokemonRandomLarge = [] # new empty list
# 1st list:
testBad_insert = [] # 1st copy


for i in range(len(text)):
	text[i] = text[i].rstrip("\n")
	
	text[i]= int(text[i])
	testBad_insert.append(text[i])


# 2nd list
file = open("testrandom.csv", "r") # for each of the 3 files
text = file.readlines()

test_random_insert = [] # 1st copy


for i in range(len(text)):
	text[i] = text[i].rstrip("\n")
	
	text[i]= int(text[i])
	test_random_insert.append(text[i])

# 3rd:
    
file = open("deleteNodes.csv", "r") # for each of the 3 files
text = file.readlines()

test_delete = [] # 1st copy

for i in range(len(text)):
	text[i] = text[i].rstrip("\n")
	
	text[i]= int(text[i])
	test_delete.append(text[i])
    
        # insert some of the bst
        # then delete some parts
        # and test the bst
        
        # and red and black trees
        # follow the psuedo code

# and more work on project2:
        
    # function to:
        #1 insert - practice by hand!!
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
            
    #next insert:
def Insert( T , node ): # change data to something better                 # T - trees node, and z named data
    Y = nil  
    X = T.head
    while X != nil:
        Y = X
        if node.data < X.data: # data is the val assigned to that node
            X = X.left
        else:
            X = X.right
        
    node.parent = Y
    
    if Y == nil:
        T.head = node # if empty
        
    elif node.data < Y.data:
        Y.left = node 
    else:
        Y.right = node
    
    # transplant next:
def transplant( T, oldRoot, newRoot ): # u - old and v - new
    if oldRoot.parent == nil:
        T.head = newRoot
    elif oldRoot == oldRoot.parent.left:
        oldRoot.parent.left = newRoot
    else:
        oldRoot.parent.right = newRoot
    if newRoot != nil:
        newRoot.parent = oldRoot.parent
        
def minValue(node): # going from child to child
        
    # loop down to find the leftmost leaf
    while(node.left is not None):
        node = node.left
    return node

def deletion( T, node ):
    if node.left == nil:
        transplant(T, node, node.right)
    elif node.right == nil:
        transplant(T, node, node.left)
    else:
        Y = minValue( node.right )
        
        if Y.parent != node:
        
            transplant(T, Y, Y.right)
        
            Y.right = node.right
        
            Y.right.parent = Y
    
        transplant(T, node, Y)
        Y.left = node.left
        Y.left.parent = Y
        
def search (node_curr, val_lookup): # x - node, k - val
    if node_curr == nil or val_lookup == node_curr.data: # need fix
        return node_curr                                # read sudo code
    
    if val_lookup < node_curr.data:
        return search(node_curr.left, val_lookup)
    else:
        return search(node_curr.right, val_lookup)
    
def height(head):
    
    if head == None:
        return 0
    else:
        
        left = height (head.left)
        right = height ( head.right )
        
        if ( left > right ):
            
            return left+1
        else:
            return right+1
        
    
#1 plus I need a function to find the height of the tree:

#2 add a function to input the csv files.

# tests
'''
t = LinkedList() # makes new tree obj
    
    # insert:
inserting = Node(10)

Insert(t, inserting)
inserting = Node(8)

Insert(t, inserting)
inserting = Node(7)

Insert(t, inserting)
inserting = Node(9)

Insert(t, inserting)
inserting = Node(11)

Insert(t, inserting)
inserting = Node(12)

Insert(t, inserting)

inorder(t.head)
print("\n\n")
deleting = search(t.head, 10)

deletion(t, deleting)

inorder(t.head)
'''
 # tree1
myTree = LinkedList() # plus add to red_and_blk
for i in testBad_insert:
    print("inserting " + str(i))
    Insert(myTree, Node(i)) # t for tree
    
print("\n\n")
inorder(myTree.head)
print("\n\n")

height_of_tree = height(myTree.head)

print(height_of_tree)
print("\n")
# plus insert again: and need

myTree_random = LinkedList()
for i in test_random_insert:
    print("inserting " + str(i))
    Insert(myTree_random, Node(i)) # t for tree
    
print("\n\n")

inorder(myTree_random.head)
print("\n\n")
print(height_of_tree)

print("\n\n")
# same for del:
i = 0
for i in range(len (test_delete) ): # change to fix 
    
    print("deleting " + str(test_delete[i])) # to fix at at [ ]
    # how -
    x = search(myTree.head, test_delete[i]) # needs fix ? interesting
    # remove search(t, Node(i)) # t for tree
    # - how:
    deletion(myTree, x)
# tree2 from both trees

# need a search before I insert
# so, i don't insert duplicate value

print("\n\n")
inorder(myTree.head) # fix why not deleting
print("\n\n")
