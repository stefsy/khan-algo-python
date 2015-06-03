'''

Breadth-first search algorithm

'''


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, obj):
        self.items.insert(0, obj)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0
    
    def list(self):
        print self.items


def doBFS(graph, source):
    bfsInfo = []

    for adjacency in graph:
        bfsInfo.append({
            "distance": None,
            "predecessor": None
        })

    bfsInfo[source]['distance'] = 0

    queue = Queue()
    queue.enqueue(source)
    
    while(queue.isEmpty() != True):
        current_vertex  = queue.dequeue()
        vertex_neighbors = graph[current_vertex]

        for v in vertex_neighbors:
            if bfsInfo[v]['distance'] == None: # hasn't been visited yet
                queue.enqueue(v)
                bfsInfo[v]['distance'] = bfsInfo[current_vertex]['distance'] + 1   
                bfsInfo[v]['predecessor'] = current_vertex 
 
    return bfsInfo            


if __name__ == "__main__":  
    adjList = [
        [1],
        [0, 4, 5],
        [3, 4, 5],
        [2, 6],
        [1, 2],
        [1, 2, 6],
        [3, 5],
        [] ]

    bfs = doBFS(adjList, 3)
    for ind, vertex in enumerate(bfs):
        print "vertex {0}: distance = {1}, predecessor = {2}".format(
                ind, vertex['distance'], vertex['predecessor']) 


    # turn below into tests of Queue class
    # tc = Queue()
    # print tc.isEmpty()
    # tc.enqueue(10)
    # tc.enqueue(-6)
    # tc.enqueue(5)
    # tc.list()
    # print tc.dequeue()
    # tc.list() 
    # print tc.dequeue()
    # print tc.isEmpty()
   

    # tc = Queue()
    # tc.enqueue((10,4))
    # tc.enqueue((5,2))
    # tc.list()
    # print tc.dequeue() 

    
    # doBFS(range(10), 5)
    
