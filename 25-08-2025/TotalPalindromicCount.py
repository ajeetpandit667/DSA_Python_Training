

def main():
  _str = "abaxbbxaxz"
  n = len(_str)
  dp = [[0 for i in range(n)] for j in range(n)]
  # arr = [[1,2,3],[4,5,6],[7,8,9]]
  #n = len(arr)
  count = 0
  for i in range(n):
    col = i
    row = 0
    while col < n:
      #print(arr[row][col],end="")
      if row == col :
        dp[row][col] = 1
        count+=1
      elif col-row <=2 :
        if _str[row] == _str[col]:
          dp[row][col] = 1
          count+=1
      else:
        if _str[row] == _str[col]:
          if dp[row+1][col-1] == 1:
            dp[row][col] = 1
            count+=1
      col+=1
      row+=1
  print(count)
    
    
main()