
def getAllper(arr):
  n = len(arr)
  if len(arr) == 1:
    return [arr]
  ans = []
  for i in range(n):
    fe = arr[i]
    ss = arr[0:i]+arr[i+1:]
    all = getAllper(ss)
    for per in all:
      per.append(fe)
      ans.append(per)
  return ans
  



def main():
  arr = [1,2,3]
  ans = getAllper(arr)
  print(ans)

main()