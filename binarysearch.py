"""
Search an ordered list to find the index of the target value
"""

"""
Clean this up! Not a great example yet, implement more practical example 
"""

def binarysearch(ran, target):
	guess = ran[len(ran)/2] # not bothering with floor b/c these are all ints
	m_min = ran[0]
	m_max = ran[:-1]

	while guess != target:
		if guess > target:
			m_max = guess - 1 
		elif guess < target: 
			m_min = guess + 1
		guess = (m_min+m_max)/2

	return ran.index(guess)
	

if __name__ == '__main__':
	testrange = range(1000)
	testtarget = 7
	print binarysearch(testrange, testtarget)