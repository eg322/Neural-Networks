def Not(inp):
	weight = -1
	treshold = -0.5
	output = weight * inp
	if output >= treshold:
		output = 1
	else:
		output = 0
	return output
def Or(inp1, inp2):
	weight = 1
	treshold = 1
	output = weight * inp1 + weight * inp2
	if output >= treshold:
		output = 1
	else:
		output = 0
	return output
def And(inp1, inp2):
	weight = 0.5
	treshold = 1
	output = weight * inp1 + weight * inp2
	if output >= treshold:
		output = 1
	else:
		output = 0
	return output
def Xor(inp1, inp2):
	output = And(Or(inp1, inp2), Or(Not(inp1), Not(inp2)))
	return output
def Then(inp1, inp2):
	output = Or(Not(inp1), inp2)
	return output
def Equal(inp1, inp2):
	output = And(Then(inp1, inp2), Then(inp2, inp1))
	return output
