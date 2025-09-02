
largestPath = ""
shortestPath = ""
minCost = float('+inf')
maxCost = float('-inf')


def multiSolver(graph,src,des,visited,psf,csf):
  global largestPath
  global shortestPath
  global minCost
  global maxCost
  if src == des:
    if csf < minCost: minCost = csf
    if csf > maxCost: maxCost = csf
    if len(psf) > len(largestPath):
      largestPath = psf
    if len(shortestPath) == 0 or len(psf) < len(shortestPath):
      shortestPath = psf
    print(psf)
    return
  visited[src] = 1
  nbrsArray = graph[src]
  for i in range(len(nbrsArray)):
    if nbrsArray[i] != 0 and visited[i] == 0:
      multiSolver(graph,i,des,visited,psf+"->"+str(i),csf+nbrsArray[i])
  visited[src] = 0


def isPathExist(graph,src,des,visited):
  if src == des:
    return True
  visited[src] = 1
  nbrsArray = graph[src]
  for i in range(len(nbrsArray)):
    if nbrsArray[i] != 0 and visited[i] == 0:
      currAns = isPathExist(graph,i,des,visited)
      if currAns == True:
        return True
  return False



      
def printGraph(graph):
  for row in graph:
    for v in row:
      print(v,end=" ")
    print()



def buildGraph(edges,n):
  graph = [[0 for i in range(n)] for j in range(n)]
  for edge in edges:
    src = edge[0]
    des = edge[1]
    wt = edge[2]
    graph[src][des] = wt
    graph[des][src] = wt
    
  return graph
    
def bfs(n,graph,src):
  queue = []
  visited = [0 for i in range(n)]
  queue.append([src,str(src)])
  while len(queue) != 0:
    poppedNode = queue.pop(0)
    cd = poppedNode[0]
    psf = poppedNode[1]
    visited[cd] = 1
    print(cd,"path---------------",psf)
    nbrsArray = graph[cd]
    for i in range(len(nbrsArray)):
      if nbrsArray[i] != 0 and visited[i] == 0:
        queue.append([i,psf+"->"+str(i)])
    
    

def main():
  global largestPath
  global shortestPath
  global minCost
  global maxCost
  edges = [[0,1,10],[1,3,4],[2,3,34],[0,2,2],[3,4,199],[4,5,23],[4,6,45],[6,7,23],[5,7,34]]
  n = 8
  graph = buildGraph(edges,n)
  #printGraph(graph)
  visited = [0 for i in range(n)]
  src = 1
  des = 7
  #ans = isPathExist(graph,0,6,visited)
  #print(ans)
  # multiSolver(graph,src,des,visited,str(src),0)
  # print("largest",largestPath)
  # print("shortest",shortestPath)
  # print("minCost",minCost)
  # print("maxCost",maxCost)
  bfs(n,graph,src)
main()