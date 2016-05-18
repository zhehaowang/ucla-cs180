import os
import sys

def maxSum(list, maxTillHere):
  if len(list) == 1:
    return max(list[0], 0)
  maxTillHere = max(0, maxTillHere + list[0])
  return max(maxSum(list[1:], maxTillHere), maxTillHere)

if __name__ == "__main__":
  print maxSum([-2, 2, -1, 4, -1, 2, 1, -5, 4], 0)