class Node:
	def __init__(self, data = None, dataSet = None):
		self.data = data
		self.dataSet = dataSet
		self.left = None
		self.right = None
	
	def getData(self):
		return self.data
	
	def getDataSet(self):
		return self.dataSet

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def setData(self, data = None):
		self.data = data

	def setDataSet(self, dataSet = None):
		self.dataSet = dataSet

	def setLeft(self, left = None):
		self.left = left

	def setRight(self, right = None):
		self.right = right

class BinaryTree:
	def __init__(self):
		self.root = None
		self.num = 0

	def size(self):
		return self.num

	def isEmpty(self):
		if self.num:
			return True
		return False

	def _insert(self, curr, node):
		if curr == None:
			self.num += 1
			return node
		elif curr.getData() > node.getData():
			temp = self._insert(curr.getLeft(), node)
			if temp != None:
				curr.setLeft(temp)
		elif curr.getData() < node.getData():
			temp = self._insert(curr.getRight(), node)
			if temp != None:
				curr.setRight(temp)

	def insert(self, node):
		temp = self._insert(self.root, node)
		if temp != None:
				self.root = temp

	def _find(self, curr, big, small, node):
		if curr == None:
			if node.getData() - small.getData() < big.getData() - node.getData():
				return small
			return big
			
		elif curr.getData() > node.getData():
			return self._find(curr.getLeft(), curr, small, node)
		elif curr.getData() < node.getData():
			return self._find(curr.getRight(), big, curr, node)
		else:
			return curr

	def find(self, node):
		return self._find(self.root, None, None, node)

a = BinaryTree()
a.insert(Node(10.5, 10))
a.insert(Node(10.5, 10))
a.insert(Node(11.1, 10))
a.insert(Node(10.1, 10))
a.insert(Node(10.7, 10))
print(a.size())
b = a.find(Node(10.5, 0))
print(b.getData())
b = a.find(Node(10.4, 0))
print(b.getData())
b = a.find(Node(10.2, 0))
print(b.getData())
b = a.find(Node(10.6, 0))
print(b.getData())
b = a.find(Node(10.8, 0))
print(b.getData())
b = a.find(Node(11, 0))
print(b.getData())