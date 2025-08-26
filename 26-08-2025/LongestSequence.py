


def getLength(arr):
  myDict = {}
  for e in arr: myDict[e] = 1
  ans = 0
  for e in arr:
    if e-1 not in myDict:
      count = 0
      n = e
      while n in myDict:
        count+=1
        n+=1
      if count > ans : ans = count
  return ans

def main():
  arr = [7,8,3,2,1,4,5,6,10,13,12,50,52,53,54]
  ans = getLength(arr)
  print(ans)
  
main()