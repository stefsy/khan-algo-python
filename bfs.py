'''

Breadth-first Search:

Learn how to traverse a graph using breadth-first-search 
to find a particular node or to make sure you've visited 
all the notes, traversing one layer at a time.

https://www.khanacademy.org/computing/computer-science/algorithms/breadth-first-search


'''


class Queue(object):
    def __init__(self):

    def enqueue(self, obj):

    def dequeue(self):

    def isEmpty(self):

    def list(self):


def doBFS(graph, source):
    """ good luck! """


if __name__ == "__main__":
    adjList = [
        [1],
        [0, 4, 5],
        [3, 4, 5],
        [2, 6],
        [1, 2],
        [1, 2, 6],
        [3, 5],
        []]

    bfs = doBFS(adjList, 3)
    for ind, vertex in enumerate(bfs):
        print "vertex {0}: distance = {1}, predecessor = {2}".format(
            ind, vertex['distance'], vertex['predecessor'])
