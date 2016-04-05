import os, sys

# Test for elementary school division

# Recursive version
def division_recursive(a, b):
  if a < 10 * b:
    return a / b
  else:
    temp = division_recursive(a, 10 * b)
    return temp * 10 + division_recursive(a - 10 * b * temp, b)

# Iterative version
def divison_iterative(a, b):
  temp = b
  stack = []
  while a > 10 * temp:
    stack.append(temp)
    temp = temp * 10

  res = a / temp
  #print str(a) + " / " + str(temp)
  result = res
  while len(stack) > 0:
    res = a - temp * result
    temp = stack.pop()
    #print str(res) + " / " + str(temp)
    res = res / temp
    result = result * 10 + res

  return result

if __name__ == "__main__":
  result = divison_iterative(10000, 9)
  print result