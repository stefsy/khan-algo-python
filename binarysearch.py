"""
Search an ordered list to find the index of the target value
"""

def basic_binary_search(array, target):
	guess = array[len(array)/2] # not bothering with floor b/c these are all ints
	m_min = array[0]
	m_max = array[:-1]

	while guess != target:
		if guess > target:
			m_max = guess - 1 
		elif guess < target: 
			m_min = guess + 1
		guess = (m_min+m_max)/2

	return array.index(guess)
	

if __name__ == '__main__':		
	print "hello i'm running the program"
	testrange = range(1000)
	testtarget = 7
	print basic_binary_search(testrange, testtarget)
