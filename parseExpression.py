from Stack import Stack
from BinaryTree import BinaryTree
import operator

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

def evaluate(parseTree):
    operators = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv}
    leftc = parseTree.getLeftChild()
    rightc = parseTree.getRightChild()
    if leftc and rightc:
        fn = operators[parseTree.getRootVal()]
        return fn(evaluate(leftc), evaluate(rightc))
    else:
        return parseTree.getRootVal()

t = parseExpression(' ( 3 + ( 4 * 5 ) )')
t.postorder()
print "Value of the expression is", evaluate(t);
