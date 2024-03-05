class Graph:
   def __init__(self, graph, heuristicNodeList, startNode):
       self.graph = graph
       self.H = heuristicNodeList
       self.start = startNode
       self.parent = {}
       self.status = {}
       self.solutionGraph = {}

   def applyAOStar(self):
       self.aoStar(self.start, False)

   def getNeighbours(self, v):
       return self.graph.get(v,'')

   def getStatus(self, v):
       return self.status.get(v, 0)

   def setStatus(self, v, val):
       self.status[v] = val

   def getHeuristicNodeValue(self, n):
       return self.H.get(n,0)

   def setHeuristicNodeValue(self, n, value):
       self.H[n] = value

   def printSolution(self):
       print("FOR GRAPH SOLUTION, TRAVERSE THE GRAPH FROM THE START NODE: ",self.start)
       print("------------------------------------------------------------")
       print(self.solutionGraph)
       print("------------------------------------------------------------")

   def computeMinimumChildNodes(self, v):
       minimumCost = 0
       costToChildNodeListDict = {}
       costToChildNodeListDict[minimumCost] = []
       flag = True
       for nodeInfoTupleList in self.getNeighbours(v):
           cost = 0
           nodeList = []
           for c, weight in nodeInfoTupleList:
               cost = cost + self.getHeuristicNodeValue(c) + weight
               nodeList.append(c)
           if flag==True:
               minimumCost = cost
               costToChildNodeListDict[minimumCost] = nodeList
               flag = False
           else:
               if cost < minimumCost:
                   minimumCost = cost
                   costToChildNodeListDict[minimumCost] = nodeList
       return minimumCost, costToChildNodeListDict[minimumCost]

   def aoStar(self, v, backTracking):
       print("HEURISTIC VALUES: ", self.H)
       print("SOLUTION GRAPH: ",self.solutionGraph)
       print("PROCESSING NODE: ",v)
       print("----------------------------------------------------------------------")
       if self.getStatus(v) >= 0:
           minimumCost, childNodeList = self.computeMinimumChildNodes(v)
           print(minimumCost, childNodeList)
           self.setHeuristicNodeValue(v, minimumCost)
           self.setStatus(v, len(childNodeList))
           solved = True
           for childNode in childNodeList:
               self.parent[childNode] = v
               if self.getStatus(childNode) != -1:
                   solved = solved & False
           if solved==True:
               self.setStatus(v, -1)
               self.solutionGraph[v] = childNodeList
           if v!=self.start:
               self.aoStar(self.parent[v], True)
           if backTracking==False:
               for childNode in childNodeList:
                   self.setStatus(childNode, 0)
                   self.aoStar(childNode, False)

print("GRAPH - ")
h = {'A': 1, 'B': 6, 'C': 2, 'D': 12}
graph = {
   'A': [[('B', 1), ('C', 3), ('D', 7)]],
   'B': [[('D', 5)]],
   'C': [[('D', 12)]]
}
graph_var = Graph(graph, h, 'A')
graph_var.applyAOStar()
graph_var.printSolution()
