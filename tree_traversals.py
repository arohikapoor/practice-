def bft(root):
	Q = new Queue()
	enqueue root
	while Q is not empty
		node = Q.dequeue()
		visit(node)
		enqueue node’s left and right children


def stack_preorder(root):
	S = new Stack()
	enqueue root
	while S is not empty
		node = Q.pop()
		visit(node)
		enqueue node’s left and right children

# pre-order: 
	#visits each node before visiting left and right
def recursive_preorder(node):
	visit(node)
	if node has left child
		preorder(node.left)
	if node has right child
		preorder(node.right)

# post-order: 
	#visits each child before visiting node
def postorder(node):
	if node has left child
		postorder(node.left)
	if node has right child
		postorder(node.right)
	visit(node)

# in-order: 
	#visits left child, node and then right child
def inorder(node):
	if node has left child
		inorder(node.left)
	visit(node)
	if node has right child
		inorder(node.right)


#perfect tree 
#Heaps
#Graphs & Topsort
#MST and Shortest Paths 
#Cracking the coding interview!!




#Validating a binary search tree
#Is node in bounds. Label children. Call on children. 
def isBST(node):
	if node.isRoot():
		node.lowerBound = -inf
		node.upperBound = inf

	if validate(node):
		if node.left == None and node.right == None:
			return True
		
		if node.left: 
			node.left.lowerBound = node.lowerbound
			node.left.upperBound = node.data
		
		if node.right: 
			node.right.lowerBound = node.data
			node.right.upperBound = node.upperbound
		
		return isBST(node.left) and isBST(node.right)

	else:
		return False

def validate(node):
	if node.data > node.lowerBound 
	and node.data < node.upperBound:
		return True
	return False

#Searching for successor (not just in lower subtree, 
#like inorder successor but in whole tree)
#Successor: smallest thing in tree greater than node
def successor(node, root):
	#If successor exists in lower subtree
	if node.right:
		curr = node.right
		while (curr.left != None):
			curr = curr.left
		return curr

	#Search in rest of the subtree
	else:
		labelBounds(root)
		successorData = node.upperBound
		if successorData == inf:
			return None
		return searchNode(root, successorData)


def searchNode(node, data):
	if node.data = data:
		return node

	left_search, right_search = None
	if node.left: left_search = searchNode(node.left)
	if node.right: right_search = searchNode(node.right)
	
	if left_search == None:
		if right_search == None: return None
		else: return right_search
	else: return left_search

#Searching for the predecessor: 
#similar logic as above except left and then RIGHT or lowerbounds

##############


#go through permutations, trip question , recursive edit distance, palindromic subsequence 
#code the facebook - recursively and iteratively  + learn to represent a tree as 
#revise on tree + graph theory uptil that day 
#go through shortest distance and MST
#convert : edge list, adjacency list, matrix
#rest of cracking the coding just read through
#understand 4.9 , 2.4 potentially

##############

#is there a path between two nodes -- bft queue 
#is there a path containing only x,y,z nodes 

##############


#Graph BFT & DFT
#Graph is_route() and num_stops() -- queue() using BFT
#Topsort ( stack or queue doesn't matter, put in a list everytime you dequeue / pop . Put in queue when no edges left to it )


#understand the alternative validate
#understand the inorder successor
#did I get 4.12 and 4.8 right? check online
#maybe do 4.10, 4.11

