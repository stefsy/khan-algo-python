
import unittest

# have a selectionsort.py file in the same folder
import selectionsort 

class SelectionSortTest(unittest.TestCase):

	def test_zero_array(self):
		self.assertEqual([0,1,2,3,4], selectionsort.selectionSort([2,1,3,4,0]))

	def test_negatives(self):
		self.assertEqual([-10,1,2,3,4], selectionsort.selectionSort([2,1,3,-10,4,]))

	def test_duplicates(self):
		self.assertEqual([1,1,2,3,3,4], selectionsort.selectionSort([2,1,3,4,1,3]))


if __name__ == '__main__':
	unittest.main() 