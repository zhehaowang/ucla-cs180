import os, sys

# Test for scheduling tournament
day = dict()

def master(num):
  listN = []
  for i in range(0, num):
    listN.append(i)
  schedule(listN)

def schedule(listN):
    if len(listN) == 1:
      return [listN[0]]
    print "0 - " + str(len(listN)/2)
    print str(len(listN)/2) + " - " + str(len(listN))
    
    merge(schedule(listN[0:len(listN)/2]), schedule(listN[len(listN)/2:len(listN)]))
    return listN

def merge(listA, listB):
    for j in range(len(listA), 2 * len(listA)):
      for i in range(0, len(listA)):
        if j in day:
          day[j].append(str(listA[i]) + " " + str(listB[(i+j) % len(listB)]))
        else:
          day[j] = [str(listA[i]) + " " + str(listB[(i+j) % len(listB)])]

if __name__ == "__main__":
  master(8)
  print day