# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 18:12:12 2022

@author: segal
"""
nil = None

class Node:
    def __init__(self, data):
        self.data = data # use data as a key
        # ex. self.ref = None
        self.left = None
        self.right = None
        self.parent = None # the parent is the val or value 
        # add color
        self.color = "red" # versuses blk
        
    
class LinkedList: # this the tree (T) # notes to fix
    def __init__(self):
        
        self.nil = Node(-1)          
        self.nil.color = "black"
        self.nil.left = None
        self.nil.right = None

        self.head = self.nil         
        
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
        
# 1st the insert function or fix_up:
# in-order:
def leftRotate( T , x ):
    
    y = x.right
    x.right = y.left
    if y.left != T.nil:
        y.left.parent = x
    y.parent = x.parent
    
    if x.parent == None:
        T.head = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y
    
def rightRotate ( T, x ): # same swap left for right
                            # and vice versa!
    # careful here:                        
    y = x.left
    x.left = y.right
    if y.right != T.nil:
        
        y.right.parent = x
    y.parent = x.parent
    
    if x.parent == None:
        T.head = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y
    
# 2nd insertion:
# + fixing_up:
def inserting( T, z ): # z is the node to insert:
    y = None
    x = T.head
    while (x != T.nil):
        y = x
        if z.data < x.data:
            x = x.left
        else:
            x = x.right
    z.parent = y
    
    if y == None:
        T.head = z
    elif z.data < y.data:
        y.left = z
    else:
        y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = "red" # for the RED color
    
    if z.parent == None:
        z.color = "black"
        return
    if z.parent.parent == None:
        return
    # call fix_up
    
    insertFix( T , z )
    
def insertFix(T,z):
    while z.parent.color == "red":
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            if y.color == "red":
                z.parent.color = "black"
                
                y.color = "black"
                z.parent.parent.color = "red"
                z = z.parent.parent
            else:
            # not this change it elif z == z.parent.right:
                # add comment fix!
                if z == z.parent.right:
                
                    z = z.parent
                    leftRotate(T,z)
                
                z.parent.color = "black"
                z.parent.parent.color = "red"
                rightRotate(T, z.parent.parent)
            
        else: # and swap left and right 2nd:
            
            y = z.parent.parent.left
            if y.color == "red":
                z.parent.color = "black"
                y.color = "black"
                z.parent.parent.color = "red"
                z = z.parent.parent
            # fixer elif z == z.parent.left:
            # add comments on fix !    
            else:  
                
                if z == z.parent.left:
                    
                    z = z.parent
                    rightRotate(T,z)
                z.parent.color = "black"
                z.parent.parent.color = "red"
                leftRotate(T, z.parent.parent)
        if z == T.head:
            break
        
    T.head.color = "black"
        
# next newTransplant:
def newTransplant( T, oldRoot, newRoot ):
    
    if oldRoot.parent == None:
        T.head = newRoot 
    elif oldRoot == oldRoot.parent.left:
        oldRoot.parent.left = newRoot
    else:
        oldRoot.parent.right = newRoot
    newRoot.parent = oldRoot.parent
    
# 1. delete
# new var for og color

def delete(T,z): 
    y = z
    
    y_original_color = y.color
    if z.left == T.nil:
        x = z.right
        newTransplant(T, z, z.right)
    elif z.right == T.nil:
        z = z.left
        newTransplant(T, z, z.left)
    else:
        y = minValue(T, z.right)
        y_original_color = y.color # might  make this a copy
        x = y.right
        if y.parent == z:
            x.parent = y
        else:
            newTransplant(T, y, y.right)
            y.right = z.right
            y.right.parent = y
        newTransplant(T, z, y)
        y.left = z.left
        y.left.parent = y
        y.color = z.color # bc y_og_color _ might mess up
    if y_original_color == "black":
        del_fix(T,x)
            
def del_fix(T, x):
    while (x != T.head and x.color == "black"):
        if x == x.parent.left:
            w = x.parent.right # and w is the uncle, x's sibling
            
            if w.color == "red":
                w.color= "black"
                
                x.parent.color = "red"
                leftRotate(T,x.parent)
                w = x.parent.right
            if w.left.color == "black" and w.right.color == "black":
                w.color = "red"
                x = x.parent
            else:
                if w.right.color == "black":
                    w.left.color = "black"
                    w.color = "red"
                    rightRotate(T, w)
                    w = x.parent.right
                
            # next on the first if's indent:
                w.color = x.parent.color
                x.parent.color = "black"
                w.right.color = "black"
                leftRotate(T,x.parent)
                x = T.head
        else:
            # and swap right and left:
            w = x.parent.left # and w is the uncle, x's sibling
            
            if w.color == "red":
                w.color= "black"
                
                x.parent.color = "red"
                rightRotate(T,x.parent) # think the rotates 
                                        #change from left to right too ?
                w = x.parent.left
            if w.right.color == "black" and w.left.color == "black":
                w.color = "red"
                x = x.parent
            else:
                if w.left.color == "black":
                    w.right.color = "black"
                    w.color = "red"
                    leftRotate(T, w)
                    w = x.parent.left
                
            # next on the first if's indent:
                w.color = x.parent.color
                x.parent.color = "black"
                w.left.color = "black"
                rightRotate(T,x.parent)
                x = T.head
            
    x.color = "black"
    
# 2. inorder_traver same
def inorder(T, root):
    if root != T.nil:
        inorder(T, root.left)
        print(root.data,end=" ")
        inorder(T, root.right)

# 3. search same
def search (T, node_curr, val_lookup): # x - node, k - val
    if node_curr == T.nil or val_lookup == node_curr.data: # need fix
        return node_curr                                # read sudo code
    
    if val_lookup < node_curr.data:
        return search(T , node_curr.left, val_lookup)
    else:
        return search(T , node_curr.right, val_lookup)
            
# 4. treeMin
def minValue(T, node): # going from child to child
        
    # loop down to find the leftmost leaf
    while(node.left != T.nil):
        node = node.left
    return node

# function for height():
def height_of_blk ( Tree, node ):
    
    counter = 0
    while node.left != Tree.nil:
        if node.color == "black":
            
            counter += 1
        
        node = node.left
        
    return counter+1

 # tree1
myTree = LinkedList() # plus add to red_and_blk
for i in testBad_insert:
    print("inserting " + str(i))
    inserting(myTree, Node(i)) # t for tree
print("\n\n")
print("The red_blk height: \n")
h = height_of_blk(myTree, myTree.head)

print(h)

print("\n\n")

inorder(myTree, myTree.head)


print("\n\n")
# plus insert again: and need
myTree_random = LinkedList()
for i in test_random_insert:
    print("inserting " + str(i))
    inserting(myTree_random, Node(i)) # t for tree
print("\n\n")

print("The red_blk height: \n")

h = height_of_blk(myTree, myTree.head)

print(h)

print('\n')

inorder(myTree_random, myTree_random.head)
print('\n\n')
# same for del:
i = 0
for i in range(len (test_delete) ): # change to fix 
    
    print("deleting " + str(test_delete[i])) # to fix at at [ ]
    # how -
    x = search(myTree, myTree.head, test_delete[i]) # needs fix ? interesting
    # remove search(t, Node(i)) # t for tree
    # - how:
    delete(myTree, x)
print('\n')
    
inorder(myTree, myTree.head)

print("\n\nThe red_blk height: \n")

h = height_of_blk(myTree, myTree.head)

print(h)
print('\n')
'''
# 2nd next test deleting in the random_case_tree: ? need fix ask Dr. H

i = 0
for i in range(len (test_delete) ): # change to fix 
    
    print("deleting " + str(test_delete[i])) # to fix at at [ ]
    # how - it works:
        
    x = search(myTree_random, myTree_random.head, test_delete[i]) # needs fix ? interesting
    # remove search(t, Node(i)) # t for tree
    # - how:
    delete(myTree_random, x)
print('\n')
    
inorder(myTree_random, myTree_random.head)
print("\nThe red_blk height: \n")
h = height_of_blk(myTree_random, myTree_random.head)
print(h)
print('\n')
'''
print(test_delete)