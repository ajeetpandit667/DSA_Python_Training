
def expandNode(zooland,i,j,m,n,visited):
  if i<0 or i>=m or j<0 or j >= n  or visited[i][j] == 1 or zooland[i][j] == 0:
    return
  visited[i][j] = 1
  expandNode(zooland,i+1,j,m,n,visited)
  expandNode(zooland,i-1,j,m,n,visited)
  expandNode(zooland,i,j+1,m,n,visited)
  expandNode(zooland,i,j-1,m,n,visited)
def main():
  zooland = [[1,1,0,0,0,0,0,0],[1,1,0,1,1,0,0,0],[0,0,1,1,0,0,0,0],[0,0,0,0,1,1,1,0],
              [1,1,0,1,1,0,0,0],[1,1,0,0,0,1,0,0]
             ]
  m = len(zooland)
  n = len(zooland[0])
  #print(m,n)
  visited = [[0 for i in range(n)] for j in range(m)]
  ans = 0
  for i in range(m):
    for j in range(n):
      if zooland[i][j] == 1 and visited[i][j] == 0:
        expandNode(zooland,i,j,m,n,visited)
        ans+=1
  print(ans)
  
main()