"""
Binary Search: 

Search an ordered list to find the index of the target value
"""

def basic_binary_search(array, target):
    guess = array[len(array)/2] # value in the middle of the array 
    m_min = array[0] 
    m_max = array[-1]

    while guess != target:
        if guess > target:
            m_max = guess - 1 
        elif guess < target: 
            m_min = guess + 1
        else: 
            raise ValueError("Loop's gone wrong!")
        guess = (m_min + m_max)/2

    return array.index(guess) 
    

if __name__ == '__main__':
    print "Enter a number between 1 and 9,999...."
    search_space = range(10000)
    target = int(raw_input())
    print "Searching for the position of {0} in a list of 10,000 numbers...".format(target)
    target_location = basic_binary_search(search_space, target)
    print "{0} is located at search_space index position {1}".format(target, target_location)
