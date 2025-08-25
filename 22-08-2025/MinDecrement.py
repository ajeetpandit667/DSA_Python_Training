

def main():
  arr = [9,17,8,2,6,8,4,5]
  wholeXor = 0
  for e in arr: wholeXor^=e
  isAnsPossible = False
  ans = float("+inf")
  index = -1
  for i in range(len(arr)):
    e = arr[i]
    xorExceptE = wholeXor ^e
    if xorExceptE <=e:
      isAnsPossible = True
      cAns = e - xorExceptE
      if cAns < ans :
        ans = cAns
        index = i
  if isAnsPossible == False:
    print(-1)
  else:
    print(ans,index)
  
main()
      