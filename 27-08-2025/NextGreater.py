


def getAllNextGreater(arr):
  st = []
  ans = [-1 for i in range(len(arr))]
  for i in range(len(arr)):
    if len(st) == 0 or st[-1][1] >= arr[i]:
      st.append([i,arr[i]])
    else:
      while len(st) > 0 and st[-1][1] < arr[i]:
        poppedEle = st.pop()
        print(poppedEle)
        ans[poppedEle[0]] = arr[i]
      st.append([i,arr[i]])
  return ans
#[5, 5, 5, 8, 9, 19, 21, 21, -1, -1, -1]    

def main():
  arr = [3,2,-1,5,8,9,19,2,21,3,8]
  ans = getAllNextGreater(arr)
  print(ans)
  
main()