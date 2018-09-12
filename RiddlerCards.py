#Generalized Riddler problem from 9/7/2018
#You have N total cards in a set, come in packs of c, how many packs on avg to get all cards?

#Calculates nCr, useful for calculations. Loops r times rather than factorials, which is slow
def combo(n, r):
	R = min(r, n - r)
	if r > n:
		return 0
	result = 1
	for i in range(R):
		result = result * (n - i) // (i + 1)
	return result

def perm(n, r):
	if r > n:
		return 0
	result = 1
	for i in range(r):
		result = result * (n - i)
	return result


#Calculates the probability of getting EXACTLY y new cards given x new cards left
#Choose y slots out of c to be new, thats cCy, then we multiply by combos of y new and c-y old
#There are xPy combos of new cards, (N-x)P(c-y) combos of new cards, and NPc combos of cards
def prob(x, y):
	return (combo(c, y) * perm(x, y) * perm(N-x, c-y) / perm(N, c))

#Builds an array of expected values (saves on function calls by memoizing)
#If you start with x left to get, you can between 0 and 10 new ones.
#So a state E[X] comes from E[X]P(0) + E[X-1]P(1) + ... E[X-10]P(10) + 1, or
#E[X] = (E[X - 1]P(1) + ... + 1) // (1 - P(0))
def EV(x):
	EVs = [0]
	if x == 0:
		return 0
	for i in range(1, x+1):
		if i < 10:
			sum = 0
			for y in range(1, i+1):
				sum  = sum + prob(i, y) * EVs[i - y]
			new = (sum + 1) / (1 - prob(i, 0))
			EVs.append(new)
		else:
			sum = 0
			for y in range(1, 11):
				sum  = sum + prob(i, y) * EVs[i - y]
			new = (sum + 1) / (1 - prob(i, 0))
			EVs.append(new)
	return(EVs)


N = 100
c = 10
print(EV(100)[100])

N = 300
print(EV(300)[300])