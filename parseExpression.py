from Stack import Stack
from BinaryTree import BinaryTree

def parseExpression(expression):
	tokens = expression.split()
	stack = Stack()
	tree = BinaryTree('')
	stack.push(tree)
	currentTree = tree
	for token in tokens:
		print token
		if token == '(':
			currentTree.insertLeft('')
			stack.push(currentTree)
			currentTree = currentTree.getLeftChild()
		elif token not in ['+', '-', '*', '/', ')']:
			currentTree.setRootVal(int(token))
			currentTree = stack.pop();
		elif token in ['+', '-', '*', '/']:
			currentTree.setRootVal(token)
			currentTree.insertRight('')
			stack.push(currentTree)
			currentTree = currentTree.getRightChild()
		elif token == ')':
			currentTree = stack.pop()
		else:
			raise ValueError
	return tree

t = parseExpression(' ( 3 + ( 4 * 5 ) )')
t.postorder()

