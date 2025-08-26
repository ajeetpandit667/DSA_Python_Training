

def printAllSubsequence(arr,i,ans):
  if i == len(arr):
    print(ans)
    return
  ans.append(arr[i])
  printAllSubsequence(arr,i+1,ans)
  ans.pop()
  printAllSubsequence(arr,i+1,ans)
  

def main():
  arr = [1,2,3]
  printAllSubsequence(arr,0,[])
  
main()