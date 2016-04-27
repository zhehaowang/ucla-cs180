import os, sys

# Test for scheduling tournament
day = dict()

def master(num):
  listN = []
  for i in range(0, num):
    listN.append(i)
  schedule(listN)

def schedule(listN):
    if listN == 1:
      return listN
    
    merge(schedule(listN/2))
    return listN

def merge(listA):
    for j in range(listA, 2 * listA):
      for i in range(0, listA):
        if j in day:
          day[j].append(str(i) + " " + str((i+j+listA) % listA))
        else:
          day[j] = [str(i) + " " + str((i+j+listA) % listA)]

if __name__ == "__main__":
  schedule(8)
  print day