import pdb

# What to do next 
# - enable calculating the postfix expression ( recognize the negative number )
# - enable accepting parenthesises
# - catch exception cases (case1. 9-2*1+2*2 - Done.) (case2. 1-1*2*3)
# - apply the GUI

class Stack:
	top = -1
	stack = []
	stack_id = ''

	def __init__(self, name):
		self.top = -1
		self.stack=[]
		self.stack_id = name

	def isFull(self):
		return self.top == 19

	def isEmpty(self):
		return self.top == -1
	
	def push(self, item):
		if self.isFull():
			print(self.stack_id, 'Stack is full. Can\'t push')

		else:
			self.top += 1
			self.stack.append(item)
	
	def pop(self):
		if self.isEmpty():
			print(self.stack_id, 'Stack is empty. Can\'t pop')

		else:
			temp = self.stack[self.top]
			del self.stack[self.top]
			self.top -= 1
			return temp

operands = Stack('OPD')
operators = Stack('OPR')

Four_oprs = ['+', '-', '*', '/']
opr_woosun = {'*': 50, '/' : 50, '+' : 40, '-' : 40, '(' : 100, ')' : 0}

while(1):
	opd1, opd2, opr = 0, 0, ''
	middle_result, middle_result2 = 0, 0
	bigopr, smallopr = '', ''
	postfix = []
	negative_flag, prnthsis_flag = False, False
	digit = []
	more_digit_number = 0
	i, j = 0, 0
	expr = input('Enter the expression to calculate.\n->')
	
	for i in range(len(expr)):

		# operator process
		if expr[i] in Four_oprs:
			if expr[i] == '-':
				operators.push('+')
				negative_flag = True
			elif expr[i] == ')':
				operators.push(expr[i])
				prnthsis_flag = True
			else:
				operators.push(expr[i])
			
		# operand process
		else:
			# if it seems like a more than 2-digit number, append the digit number to an array
			if i+1 != len(expr) and not expr[i+1] in Four_oprs:
				digit.append(int(expr[i]))
			
			# if the more than 2-digit number ends, push it to stack
			elif len(digit) > 0:
				for j in range(len(digit)):
					more_digit_number += pow(10, len(digit)-j)*digit[j]
				more_digit_number += int(expr[i])
				if negative_flag:
					operands.push(more_digit_number*(-1))
					negative_flag  = False
				else:
					operands.push(more_digit_number)
				digit = []
				more_digit_number = 0

			# when it is a 1-digit number
			else:
				if negative_flag:
					operands.push(int(expr[i])*(-1))
					negative_flag = False
				else:
					operands.push(int(expr[i]))

		# check the operators stack
		while operators.top > 0 and opr_woosun[operators.stack[operators.top]] <= opr_woosun[operators.stack[operators.top-1]]:
#if prnthsis_flag:

			if operators.top == 0:
				bigopr = operators.pop()
			else:
				smallopr = operators.pop()
				bigopr = operators.pop()
				operators.push(smallopr)

			if operands.top > 0:
				opd2 = operands.pop()
				opd1 = operands.pop()
				postfix.append(int(opd1))
				postfix.append(int(opd2))
				postfix.append(bigopr)
			elif operands.top == 0:
				opd1 = operands.pop()
				postfix.append(int(opd1))
				postfix.append(bigopr)
			else:
				postfix.append(bigopr)

	# if there remains operands in the stack, flush them all with operators
	while not operands.isEmpty():
		if operands.top == 0:
			opd1 = operands.pop()
			bigopr = operators.pop()
			postfix.append(int(opd1))
			postfix.append(bigopr)
			continue
		opd2 = operands.pop()
		opd1 = operands.pop()
		bigopr = operators.pop()
		postfix.append(int(opd1))
		postfix.append(int(opd2))
		postfix.append(bigopr)
	while not operators.isEmpty():
		postfix.append(operators.pop())

	# Print the postfix expression
	print('Postfix expression is', end = ' ')
	for item in postfix:
		print(item, end='')
	print()


	#pdb.set_trace() ## debugging break point
	opd1 = 0
	opd2 = 0
	
	# Calculate the postfix expression
	for i in range(len(postfix)):
		# when operand turn
		if type(postfix[i]) == int:
			if opd1 == 0:
				opd1 = postfix[i]
				continue
			elif opd2 == 0:
				opd2 = postfix[i]
				continue
		# when operator turn
		else:
			opr = postfix[i]
			if middle_result == 0:
				if opr == '+':
					middle_result = opd1 + opd2
				elif opr == '-':
					middle_result = opd1 - opd2
				elif opr == '*':
					middle_result = opd1 * opd2
				elif opr == '/':
					middle_result = opd1 / opd2
				opd1 = 0
				opd2 = 0

			else: # when middle_result is not 0
				if opd1 != 0 and opd2 != 0:
					if opr == '+':
						middle_result2 = opd1 + opd2
					elif opr == '-':
						middle_result2 = opd1 - opd2
					elif opr == '*':
						middle_result2 = opd1 * opd2
					elif opr == '/':
						middle_result2 = opd1 / opd2
					opd1 = 0
					opd2 = 0

				elif opd1 != 0 and opd2 == 0:
					if opr == '+':
						middle_result += opd1
					elif opr == '-':
						middle_result -= opd1
					elif opr == '*':
						middle_result *= opd1
					elif opr == '/':
						middle_result /= opd1
					opd1 = 0
				elif opd1 == 0 and opd2 == 0:
					if opr == '+':
						middle_result += middle_result2
					elif opr == '-':
						middle_result -= middle_result2
					elif opr == '*':
						middle_result *= middle_result2
					elif opr == '/':
						middle_result /= middle_result2
					middle_result2 = 0
				else:
					print('error case occured')

	print('Result is {0}'.format(middle_result))

				
