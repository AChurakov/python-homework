import operator

###############
## N5
###############

def most_popular_word():
	words = []
	while True:
		string = input()
		if not string:
			break
		else:
			words.extend([w.replace(',', '').replace(';', '').replace('!', '').replace('?', '').replace('.', '') for w in string.rsplit()])

	words_count = {}
	for word in words:
		words_count[word] = words_count[word]+1 if word in words_count else 1

	words_count = sorted(words_count.items(), key = lambda x: x[1], reverse=True)

	return '---' if len(words_count) > 1 and words_count[0][1] == words_count[1][1] else words_count[0][0]
	


##############
## N6
##############

def multiple_table(m,n):
	p = len(str(m * n))
	n_length = len(str(n))
	for i in range(1, n+1):
		print('{:_>{P}}_=_{:_>{K}}_{}'.format(i * m, i, m, P = p, K = n_length))

	return True


##############
## N7
##############

def paid_stairs(costs, step):
	if len(costs) < step:
	    return costs[-1]
	else:
		for i, v in enumerate(costs):
			if i < step:
				continue
			else:
				p = min(costs[i-step:i])
				costs[i] += p

	return costs[-1]


##############
## N8
##############

def reverse_polish_notation_calc(expr):
	try:
		OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
		stack = []
		for token in expr.split(" "):
			if token in OPERATORS:
				op2, op1 = stack.pop(), stack.pop()
				stack.append(OPERATORS[token](op1,op2))
			elif token:
				stack.append(float(token))

		return stack.pop() if len(stack) == 1 else 'ERROR'

	except:
		return 'ERROR'


##########################
###  Main
##########################


# 5
print(most_popular_word())

# 6
m, n = [int(i) for i in input().split(',')]
multiple_table(m=m,n=n)

# 7
costs = [int(x) for x in input().split(', ')]
step = int(input())
print(paid_stairs(costs=costs, step=step))

# 8
print(reverse_polish_notation_calc(input()))