
import unittest

import insertionsort 

class InsertionSortTest(unittest.TestCase):

	def test_insert_array(self):
		self.assertEqual([0,1,2,3,4], insertionsort.insert([0,1,3,4], 2, 2))

	def test_insertsort_posints(self):
		self.assertEqual([-10,1,2,3,4,4], insertionsort.insertSort([2,1,3,-10,4,4]))


if __name__ == '__main__':
	unittest.main() 

