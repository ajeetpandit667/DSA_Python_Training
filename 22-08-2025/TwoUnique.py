def getFirstSetBitpos(n):
  if n == 0: return -1
  ans = 1
  while n%2 == 0:
    n = n>>1
    ans+=1
  return ans

def getIthBit(n,i):
  n = n>> (i-1)
  return n%2


def main():
  arr = [9,18,25,9,7,7,16,16]
  wholeXor = 0
  for i in range(len(arr)): wholeXor^=arr[i]
  fsbpos = getFirstSetBitpos(wholeXor)
  ans1 = 0
  ans2 = 0
  for e in arr:
    if getIthBit(e,fsbpos) == 1:
      ans1^=e
    else:
      ans2^=e
  print(ans1,ans2)
  
main()