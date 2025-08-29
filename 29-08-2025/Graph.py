
def isPathExist(graph,src,des,visited):
  if src == des:
    return True
  visited[src] = 1
  nbrsArray = graph[src]
  for i in range(len(nbrsArray)):
    if nbrsArray[i] == 1 and visited[i] == 0:
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
    graph[src][des] = 1
    graph[des][src] = 1
    
  return graph
    


def main():
  edges = [[0,1],[1,3],[2,3],[0,2],[4,5],[4,6],[6,7],[5,7]]
  n = 8
  graph = buildGraph(edges,n)
  printGraph(graph)
  visited = [0 for i in range(n)]
  ans = isPathExist(graph,0,7,visited)
  print(ans)
main()