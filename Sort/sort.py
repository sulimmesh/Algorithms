import random

if __name__ == "__main__":
	one = [1,2,3,4,5,6,7,8,9,10]
	two = [10,9,8,7,6,5,4,3,2,1]
	three = [0]*10
	for i in range(1,11):
		rand = random.randint(0,9)
		while three[rand] > 0:
			rand = random.randint(0,9)
		three[rand] = i
	print one
	print two
	print three			