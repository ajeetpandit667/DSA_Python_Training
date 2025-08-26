


  
def nQueen(n,board,row,col,dia,rev):
  if row == n:
    for arr in board:
      for v in arr:
        print(v,end="")
      print()
    print("========================")
    print("========================")
    print("========================")
  for i in range(n):
    if col[i] == 0 and dia[row-i+n] == 0 and rev[row+i] == 0:
      board[row][i] = 'Q'
      col[i] = 1
      dia[row-i+n] = 1
      rev[row+i] = 1
      nQueen(n,board,row+1,col,dia,rev)
      board[row][i] = '0'
      col[i] = 0
      dia[row-i+n] = 0
      rev[row+i] = 0
      
      

def main():
  n = 6
  board = [[0 for i in range(n)] for j in range(n)]
  col = [0 for i in range(n)]
  dia = [0 for i in range(2*n)]
  rev = [0 for i in range(2*n)]
  nQueen(n,board,0,col,dia,rev)
  
main()