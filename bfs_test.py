
import unittest
import bfs

# tests for the queue implementation. make sure these pass before tackling doBFS()
class SimpleQueueTestCase(unittest.TestCase):
    def setUp(self):
        self.q = bfs.Queue()

class FullQueueTestCase(SimpleQueueTestCase):
    def test_created_isempty(self):
        self.assertTrue(self.q.isEmpty, msg="queue not empty on creation")

    def test_items(self):
        self.assertEqual(self.q.items, [], msg="items not initializing properly")

    def test_enqueue(self): 
        self.q.enqueue(0)
        self.assertEqual(self.q.items, [0], msg="check enqueue function")

    def test_enqueue_multiple_items(self): 
        self.q.enqueue(10)
        self.q.enqueue(-10)
        self.q.enqueue(5)
        self.assertEqual(self.q.items, [5, -10, 10], msg="check enqueue function")

    def test_dequeue(self):
        self.q.enqueue(10)
        self.q.enqueue(-10)
        self.q.enqueue(5)
        self.q.dequeue()
        self.q.dequeue()
        self.assertEqual(self.q.items, [5]) 

# testing the breadth-first search implementation
class SimpleBFSTestCase(unittest.TestCase):
    def setUp(self):
       self.adjList = [ \
        [1], [0, 4, 5],[3, 4, 5], [2, 6], \
        [1, 2], [1, 2, 6], [3, 5],[]] 


class FullBFSTestCase(SimpleBFSTestCase):
    def test_number_of_nodes(self):
        temp_bfs = bfs.doBFS(self.adjList, 3)
        self.assertEqual(len(temp_bfs), 8, msg="incorrect number of nodes in bfs graph")

    def test_predecessor(self):
        temp_bfs = bfs.doBFS(self.adjList, 3)
        self.assertEqual(temp_bfs[0]['predecessor'], 1)

    def test_vertex(self):
        temp_bfs = bfs.doBFS(self.adjList, 3)
        self.assertEqual(temp_bfs[0]['distance'], 4)


if __name__ == '__main__':
	unittest.main() 
