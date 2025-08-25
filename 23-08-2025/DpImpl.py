
def climbStairsWithDict(n,dict):
  if n in dict:
    return dict[n]
  if n <=2 :
    dict[n] = n
    return n
  x = climbStairsWithDict(n-1,dict)
  dict[n-1] = x
  y = climbStairsWithDict(n-2,dict)
  dict[n-2] = y
  return x+y
  
  




def climbStairsWithArray(n,dp):
  if dp[n] != 0: return dp[n]
  if n <= 2:
    dp[n] = n
    return dp[n]
  x = climbStairsWithArray(n-1,dp)
  dp[n-1] = x
  y = climbStairsWithArray(n-2,dp)
  dp[n-2] = y
  return x+y
  #return climbStairsWithArray(n-1)+climbStairsWithArray(n-2)


def main():
  n = 100
  # dp = [0 for i in range(n+1)]
  # ans = climbStairsWithArray(n,dp)
  dp = {}
  ans = climbStairsWithDict(n,dict)
  print(ans)
main()