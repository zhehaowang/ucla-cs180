import os, sys

# Test for find celebrity - iterative
def hasCelebrity(matrix):
  l = len(matrix)
  if l < 2:
    return -1
  i = 0
  j = 1
  
  while max(i, j) < l:
    print i, j
    if matrix[i][j] == 1 and matrix[j][i] == 0:
      i = max(i, j) + 1
    elif matrix[j][i] == 1 and matrix[i][j] == 0:
      j = max(i, j) + 1
    else:
      i = max(i, j) + 1
      j = max(i, j) + 1
    print i, j
  
  if min(i, j) >= len(matrix):
    return -1

  if i >= l:
    return isCelebrity(matrix, j)
  else:
    return isCelebrity(matrix, i)

def isCelebrity(matrix, i):
  for p in range(0, len(matrix)):
    if p != i:
      if matrix[p][i] == 0 or matrix[i][p] == 1:
        return -1
  return i

if __name__ == "__main__":
  m = [[0]*3 for i in range(3)]
  m[0][0] = 0
  m[0][1] = 1
  m[0][2] = 1

  m[1][0] = 0  
  m[1][1] = 1  
  m[1][2] = 1

  m[2][0] = 0
  m[2][1] = 0  
  m[2][2] = 0

  result = hasCelebrity(m)
  print result
