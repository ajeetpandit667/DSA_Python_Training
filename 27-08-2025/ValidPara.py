

def isValid(_str):
  st = []
  for i in range(len(_str)):
    ch = _str[i]
    if ch == '(' or ch == '[' or ch == '{':
      st.append(ch)
    else:
      if len(st) == 0:
        return False
      if ch == ')' and st[-1] != '(': return False
      if ch == '}' and st[-1] != '{': return False
      if ch == ']' and st[-1] != '[': return False
      st.pop()
  return len(st) == 0



def main():
  _str = "(((({}{[]})))"
  ans = isValid(_str)
  print(ans)
main()