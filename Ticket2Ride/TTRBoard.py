import networkx as nx
import pylab

class Board(object):
    def __init__(self):
        self.G = nx.MultiGraph()
        self.cities = ['Atlanta',        'Boston',         'Calgary',
                        'Charleston',    'Chicago',        'Dallas',     
                        'Denver',        'Duluth',         'El Paso',
                        'Helena',        'Houston',        'Kansas City', 
                        'Las Vegas',     'Little Rock',    'Los Angeles', 
                        'Miami',         'Montreal',       'Nashville',
                        'New Orleans',   'New York',       'Oklahoma City',
                        'Omaha',         'Phoenix',        'Pittsburgh',
                        'Portland',      'Raleigh',        'Saint Louis', 
                        'Salt Lake City','San Francisco',  'Santa Fe',
                        'Sault St Marie','Seattle',        'Toronto', 
                        'Vancouver',     'Washington',     'Winnipeg'
                        ]

        for city in self.cities:
            self.G.add_node(city)

        ##possible edge colors: red,     orange,     yellow, 
        #                       green,   blue,       purple, 
        #                       black,   white,      grey
        edges = [
            ('Los Angeles', 'San Francisco', 3, ['yellow', 'purple']),
            ('Los Angeles', 'Las Vegas', 2, ['grey']),
            ('Los Angeles', 'Phoenix', 3, ['grey']),
            ('Las Vegas', 'Salt Lake City', 3, ['orange']),
            ('Salt Lake City', 'Helena', 3, ['purple']),
            ('Helena', 'Winnipeg', 4, ['blue']),
            ('Helena', 'Denver', 4, ['green']),
            ('Salt Lake City', 'Denver', 3, ['red', 'yellow']),
            ('Phoenix', 'Santa Fe', 3, ['grey']),
            ('Los Angeles', 'El Paso', 6, ['black']),
            ('Phoenix', 'El Paso', 3, ['grey']),
            ('El Paso', 'Santa Fe', 2, ['grey']),
            ('Santa Fe', 'Denver', 2, ['grey']),
            ('Helena', 'Duluth', 6, ['orange']),
            ('Helena', 'Omaha', 5, ['red']),
            ('Winnipeg', 'Duluth', 4, ['black']),
            ('Winnipeg', 'Sault St Marie', 6, ['grey']),
            ('Denver', 'Omaha', 4, ['purple']),
            ('Denver', 'Kansas City', 4, ['black', 'orange']),
            ('Denver', 'Oklahoma City', 4, ['red']),
            ('Santa Fe', 'Oklahoma City', 3, ['blue']),
            ('El Paso', 'Oklahoma City', 5, ['yellow']),
            ('El Paso', 'Dallas', 4, ['red']),
            ('El Paso', 'Houston', 6, ['green']),
            ('Houston', 'Dallas', 1, ['grey', 'grey']),
            ('Dallas', 'Oklahoma City', 2, ['grey', 'grey']),
            ('Oklahoma City', 'Kansas City', 2, ['grey', 'grey']),
            ('Omaha', 'Kansas City', 1, ['grey', 'grey']),
            ('Omaha', 'Duluth', 2, ['grey', 'grey']),
            ('Duluth', 'Sault St Marie', 3, ['grey']),
            ('Duluth', 'Toronto', 6, ['purple']),
            ('Duluth', 'Chicago', 3, ['red']),
            ('Omaha', 'Chicago', 4, ['blue']),
            ('Dallas', 'Little Rock', 2, ['grey']),
            ('Oklahoma City', 'Little Rock', 2, ['grey']),
            ('Houston', 'New Orleans', 2, ['grey']),
            ('New Orleans', 'Little Rock', 3, ['green']),
            ('Little Rock', 'Saint Louis', 2, ['grey']),
            ('Kansas City', 'Saint Louis', 2, ['blue', 'purple']),
            ('Little Rock', 'Nashville', 3, ['white']),
            ('Nashville', 'Saint Louis', 2, ['grey']),
            ('Saint Louis', 'Chicago', 2, ['green', 'white']),
            ('Sault St Marie', 'Toronto', 2, ['grey']),
            ('Sault St Marie', 'Montreal', 5, ['black']),
            ('Montreal', 'Toronto', 3, ['grey']),
            ('Montreal', 'Boston', 2, ['grey', 'grey']),
            ('Montreal', 'New York', 3, ['blue']),
            ('Toronto', 'Pittsburgh', 2, ['grey']),
            ('Toronto', 'Chicago', 4, ['white']),
            ('Boston', 'New York', 2, ['yellow', 'red']),
            ('New York', 'Pittsburgh', 2, ['green', 'white']),
            ('New York', 'Washington', 2, ['orange', 'black']),
            ('Pittsburgh', 'Chicago', 3, ['orange', 'black']),
            ('Pittsburgh', 'Saint Louis', 5, ['green']),
            ('Pittsburgh', 'Nashville', 4, ['yellow']),
            ('Pittsburgh', 'Raleigh', 2, ['grey']),
            ('Pittsburgh', 'Washington', 2, ['grey']),
            ('Washington', 'Raleigh', 2, ['grey', 'grey']),
            ('Raleigh', 'Nashville', 3, ['black']),
            ('Nashville', 'Atlanta', 1, ['grey']),
            ('Atlanta', 'Raleigh', 2, ['grey', 'grey']),
            ('Raleigh', 'Charleston', 2, ['grey']),
            ('Atlanta', 'New Orleans', 4, ['yellow', 'orange']),
            ('Atlanta', 'Charleston', 2, ['grey']),
            ('Miami', 'Charleston', 4, ['purple']),
            ('Miami', 'Atlanta', 5, ['blue']),
            ('Miami', 'New Orleans', 6, ['red'])
        ]

        for edge in edges:
            source, destination, weight, colors = edge
            for color in colors:
                self.G.add_edge(source, destination, weight=weight, color=color,owner=None)


        #create a copy of the board to store the original state of the board
        self.copyBoard = self.G.copy()
        
    def showBoard(self, board, pauseTime = 7):
        """display board
        """
        pos=nx.spring_layout(board)
        nx.draw(board, pos)
        nx.draw_networkx_edge_labels(board, pos)
        pylab.ion()
        pylab.show()
        pylab.pause(pauseTime)
        pylab.close()
    
    def hasEdge(self, city1, city2):
        """returns True an edge exists between city1, city2.  False otherwise
        city1, city2: string
        """
        return self.G.has_edge(city1, city2)

    def removeEdge(self, city1, city2, edgeColor):
        """remove the edge between two cities that's colored edgeColor
        city1, city2:  string
        edgeColor:  string
        raises ValueError if edge does not exist
        """
        if not self.hasEdge(city1, city2):
            raise ValueError("Edge between %s and %s does not exist" 
                                % (city1, city2))
        
        posColors = self.getEdgeColors(city1, city2)
        
        #if the edge is grey, accept any color and remove grey
        if "grey" in posColors:
            self.G.get_edge_data(city1, city2)['colors'].remove("grey")
            if len(self.G.get_edge_data(city1, city2)['color']) == 0:
                self.G.remove_edge(city1, city2)
            
        else:
            if edgeColor not in posColors:
                raise ValueError("A %s edge does not exist between %s and %s" 
                                    % (edgeColor, city1, city2))
            
            #if edge has a color, remove that color
            self.G.get_edge_data(city1, city2)['color'].remove(edgeColor)
            if len(self.G.get_edge_data(city1, city2)['color']) == 0:
                self.G.remove_edge(city1, city2)
            
    def getEdges(self):
        """returns a list of tuples of all remaining edges', [(city1, city2)]
        """
        return self.G.edges()

    def getEdgeColors(self, city1, city2):
        """returns the edgeColors of edge
        city1, city2: string
        """
        return self.G.get_edge_data(city1, city2)['color']

    def getEdgeWeight(self, city1, city2):
        """returns the weight of the edge (i.e. the distance between two cities)
        city1, city2: string
        """
        return self.G.get_edge_data(city1, city2)['weight']
    
    def getPathWeight(self, city1, city2):
        """returns the weight of the shortest path between city1, city2
        """
        return nx.dijkstra_path_length(self.G, city1, city2)
    
    def getNodes(self):
        return self.G.nodes()

    def getCities(self):
        """returns a list of all remaining cities
        that can be traveled to or from
        """
        return self.G.nodes()
    
    def getAdjCities(self, city1):
        """returns a list of cities adjacent to city1 
        that still have available edges
        """
        return [x[1] for x in self.G.edges(city1)]
        
    def hasPath(self, city1, city2):
        """returns True if a path exists between city1 and city2
        searches self.G (the graph the class uses)
        city1, city2: String
        """
        return nx.has_path(self.G, city1, city2)
    
    def iterEdges(self):
        """returns an interator over all edges and edge data"""
        return self.G.edges(data = True)
        
class PlayerBoard(Board):
    """Creates a custom graph for each player to represent their progress"""
    def __init__(self):
        self.G = nx.Graph()
    
    def addEdge(self, city1, city2, routeDist, color):
        """
        city1, city2, color: Strings
        routeDist          : int
        """
        self.G.add_edge(city1, city2, weight = routeDist, edgeColors = [color])

    def longestPath(self, start):
        """returns a tuple: (len longestPath, tuple of cities along longestPath)
        This is a modification of BFS that uses edges instead of nodes
        It has no ending condition, rather it searches the whole graph and
        returns the weight of the longest path and the edges that of that path

        #Doctest

        >>> p = PlayerBoard()
        >>> p.addEdge('a', 'b', 1, 'blue')
        >>> p.addEdge('b', 'd', 1, 'blue')
        >>> p.addEdge('d', 'e', 1, 'blue')
        >>> p.addEdge('e', 'f', 98, 'blue')
        >>> p.addEdge('e', 'b', 1, 'blue')
        >>> p.addEdge('b', 'c', 1, 'blue')
        >>> p.addEdge('a', 'z', 1, 'blue')
        
        >>> p.longestPath('b')
        (100, (['b', 'd', 'e', 'f'], set([('d', 'e'), ('e', 'f'), ('b', 'd')])))
        
        # if p.addEdge('e', 'f', 1, 'blue')
        # (5, (['b', 'd', 'e', 'b', 'a', 'z'], \
        #    set([('b', 'a'), ('d', 'e'), ('a', 'z'), ('e', 'b'), ('b', 'd')])))

        """
        
        longestPath = (0, ())
        q = []
        
        q.append( ([start], set()) ) #( [path], set(exploredEdges) )
        
        while q:
            cur = q.pop() #pop() = DFS, pop(0) = BFS (consider Deque for O(1))
            
            if len(cur[1]) > 0:
                pathWeight = sum( [self.getEdgeWeight(x[0],x[1]) 
                                    for x in cur[1]] )
            
                if pathWeight > longestPath[0]:
                    longestPath = (pathWeight, cur)
            
            node = cur[0][-1]
            edgesExplored = cur[1]
            adjCities = set()
            for i in self.getAdjCities(node):
                #add if edge between cities not explored
                if (node, i) not in edgesExplored:
                    if (i, node) not in edgesExplored:
                        adjCities.add(i) 
            
            for suc in adjCities:
                proxy = cur[1].copy()
                proxy.add((node, suc))
                newPath = cur[0] + [suc]

                q.append((newPath, proxy)) #add to path, add edge
                    
        
        #Note: set of path edges will not be ordered
        return longestPath        

if __name__ == "__main__":
    import doctest
    doctest.testmod()