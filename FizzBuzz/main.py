"""
The classic interview problem. FizzBuzz takes a number and iterates.
If i is divisible by 3 it prints fizz, by 5 it prints buzz, by both it 
prints fizzbuzz. Nothing else to it. If you're new to programming, there
are worse places to start 
"""

def fizzbuzz(n):
	for i in range(1,n):
		remain3 = i%3
		remain5 = i%5
		if not remain3 and not remain5:
			print "FizzBuzz "
		elif not remain3:
			print "Fizz "
		elif not remain5:
			print "Buzz "
		else:
			print str(i)+" "
	print

if __name__ == "__main__":
	n = 31
	fizzbuzz(n)