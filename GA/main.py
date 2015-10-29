"""
Basis:
	Implementation of Genetic Algorithms. This specific implementation
	solves the problem of 'fitness' for a given string. The 'fitness' of
	a string is given by a set of rules supplied by the user. 'Fitness'
	always starts from 0 is increases based on succeeding pairs of chars.
	Given:
		1) 'abc'
		2) 'bac'
	Where:
		a->a = +0
		a->b = +1
		a->c = +2
		b->a = +2
		b->b = +0
		b->c = +1
		c->a = +1
		c->b = +0
		c->c = +1
	Result:
		1) 2
		2) 4
"""
import random

"""
Fitness test. Needs to run in polynomial time to be efficient

@param string -> string to test
@param rules -> dictionary of char pairings and fitnesses

returns @param fitness -> int calculated fitness
"""
def fitness(string, rules):
	fitness = 0
	for i in range(len(string)-1):
		pair = string[i]+string[i+1]
		if not pair in rules:
			raise ValueError("Incomplete rule or state set.")
		fitness += rules[pair]
	return fitness

"""
Takes two strings and returns a single string 'offspring'.
This example uses multiple crossovers and random mutations.
@param states -> a list of possible states
@param string1 -> a string to be bred
@param string2 -> a string to be bred

returns @param child -> the resulting child string
"""
def breed(states, string1, string2):
	length = len(string1[0])
	rate = 0.025
	child = ''
	cross1 = random.randint(0,length/2)
	cross2 = random.randint(cross1,length)
	mutations = random.sample(range(0,length),int(rate*length))
	for i in range(cross1):
		if i in mutations:
			new_char = random.randint(0,len(states)-1)
			child += states[new_char]
		else:
			child += string1[0][i]
	for i in range(cross1,cross2):
		if i in mutations:
			new_char = random.randint(0,len(states)-1)
			child += states[new_char]
		else:
			child += string2[0][i]
	for i in range(cross2, len(string1[0])):
		if i in mutations:
			new_char = random.randint(0,len(states)-1)
			child += states[new_char]
		else:
			child += string1[0][i]
	return child

"""
TODO

matching fn:
	1) sort by fitness
	2) create matching data structure
		hashable key -> string + index
	3) use shrinking cutoff
	4) breed from best to worst to fill out 
		an equal sized new generation
	5) return generation

doGA:
	1) randomly gen first generation
	2) while timeout > 0, run matching fn
	3) gen = new_gen
	4) sort by fitness
	5) return highest value
"""

"""
Finds a mate for a given member
@param gen -> list of generation
@param matches -> the matches dictionary
@param i -> current index
@param cutoff -> int cutoff
@param prev -> optional int index of previous partner

returns @param partner -> string matched partner
"""
def findMatch(gen, matches, i, cutoff, prev=None):
	#loop until mate is available
	loop = True
	while loop:
		index = random.randint(0,cutoff-1)
		if index == i:
			continue
		if index == prev:
			continue
		if gen[index][0]+str(index) in matches:
			if index <= len(gen)-cutoff:
				if len(matches[gen[index][0]+str(index)]) >= 4:
					continue
			else:
				if len(matches[gen[index][0]+str(index)]) >= 2:
					continue
		loop = False
	return index

"""
Creates a matched set of members to be bred. then
creates a new generation from those members.
@param states -> a list of possible states
@param gen -> a list of the current generation
@param rules -> dictionary of char pairings
@param cutoff -> int the index to cut off the list

returns @param new_gen -> a list of the next generation
"""
def match(states, gen, rules, cutoff):
	gen.sort(key=lambda x: x[1], reverse=True)
	matches = {}
	new_gen = []
	for i in range(cutoff):
		if gen[i][0]+str(i) in matches:
			if i <= len(gen)-cutoff:
				if len(matches[gen[i][0]+str(i)]) >= 4:
					continue
			else:
				if len(matches[gen[i][0]+str(i)]) >= 2:
					continue
		else:
			matches[gen[i][0]+str(i)] = []
		if i > cutoff:
			#don't breed
			continue
		index1 = findMatch(gen, matches, i, cutoff)
		if not gen[index1][0]+str(index1) in matches:
			matches[gen[index1][0]+str(index1)] = []
		if i <= len(gen)-cutoff:
			#need two random partners
			#breed twice with each
			index2 = findMatch(gen, matches, i, cutoff, index1)
			if not gen[index2][0]+str(index2) in matches:
				matches[gen[index2][0]+str(index2)] = []
			matches[gen[i][0]+str(i)].extend([gen[index1], gen[index2]])
			matches[gen[index1][0]+str(index1)].append(gen[i])
			matches[gen[index2][0]+str(index2)].append(gen[i])
			for i in range(2):
				child1 = breed(states, gen[i], gen[index1])
				child2 = breed(states, gen[i], gen[index2])
				new_gen.append([child1, fitness(child1, rules)])
				new_gen.append([child2, fitness(child2, rules)])
		else:
			#need one random partner
			#breed twice
			matches[gen[i][0]+str(i)].append(gen[index1])
			matches[gen[index1][0]+str(index1)].append(gen[i])
			child1 = breed(states, gen[i], gen[index1])
			child2 = breed(states, gen[i], gen[index1])
			new_gen.append([child1, fitness(child1, rules)])
			new_gen.append([child2, fitness(child2, rules)])
	return new_gen

"""
The central algorithm
@param states -> a list of possible char states
@param rules -> a dictionary of char pairings and fitnesses
@param length -> length of each string
@param n -> int number of strings
@param timeout -> int amount of generations to run GA

returns @param solution -> string of the highest scoring solution
"""
def doGA(states, rules, length, n, timeout):
	gen = []
	for i in range(n):
		member = ''
		for i in range(length):
			index = random.randint(0,len(states)-1)
			member += states[index]
		gen.append([member, fitness(member,rules)])
	while timeout > 0:
		gen = match(states, gen, rules, 300)
		print gen[0]
		timeout -= 1
	gen.sort(key=lambda x: x[1], reverse=True)
	return gen[0]

def main():
	states = ['a','b','c']

	rules = {
		'aa': 0,
		'ab': 1,
		'ac': 2,
		'ba': 2,
		'bb': 0,
		'bc': 1,
		'ca': 1,
		'cb': 0,
		'cc': 1
	}

	string1 = 'abc'
	string2 = 'bac'
	assert fitness(string1, rules) == 2
	assert fitness(string2, rules) == 4

	result = doGA(states, rules, 100, 500, 100)
	print result

if __name__ == "__main__":
	main()



