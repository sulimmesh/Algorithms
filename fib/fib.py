import time
def memoize(f):
	memo = {}
	def helper(x):
		if not x in memo:
			memo[x] = f(x)
		return memo[x]
	return helper

def fib_rec(x):
	if x == 1:
		return 1
	if x == 2:
		return 1
	return fib_rec(x-1)+fib_rec(x-2)

def fib_iter(x):
	if x == 2:
		return 1
	if x == 1:
		return 1
	old = 1
	older = 1
	for i in range(x-2):
		cur = old + older
		older = old
		old = cur
	return cur

def fib_memo(x, dic):
	if x == 1:
		dic[x] = 1
	if x == 2:
		dic[x] = 1
	if x not in dic:
		dic[x] = fib_memo(x-1, dic)+fib_memo(x-2, dic)
	return dic[x]

if __name__ == "__main__":
	t0 = time.time()
	for i in range(1,30):
		fib_iter(i)
	t1 = time.time()
	t2 = time.time()
	for i in range(1,30):
		fib_rec(i)
	t3 = time.time()
	fib = memoize(fib_rec)
	t4 = time.time()
	for i in range(1,30):
		fib(i)
	t5 = time.time()
	memo = {}
	t6 = time.time()
	for i in range(1,30):
		fib_memo(i, memo)
	t7 = time.time()
	print "iterative: "+str(t1-t0)+"s"
	print "raw recursive: "+str(t3-t2)+"s"
	print "memo recursive: "+str(t5-t4)+"s"
	print "internal memo: "+str(t7-t6)+"s"
