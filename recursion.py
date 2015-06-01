def fib(n):
	if n == 0: 
		return 1
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

if __name__ == '__main__':
	for n in range(10):
		print "n", n, "fib value", fib(n)