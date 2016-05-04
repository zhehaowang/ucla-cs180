import os, sys

# This work ended up referring to http://www.cs.mun.ca/~kol/courses/2711-f13/dynprog.pdf; should figure out details

def schedule_jobs(ddls, times):
  schedule = [[0 for x in range(ddls[len(ddls) - 1] + 1)] for y in range(len(ddls))] 
  # this timeline solution is not correct; accounting in knapsack seems more complicated than I thought!
  #time_line = [[0 for x in range(ddls[len(ddls) - 1] + 1)] for y in range(len(ddls))] 

  for j in range(times[0], ddls[len(ddls) - 1] + 1):
    schedule[1][j] = 1
  print schedule

  for i in range(1, len(ddls)):
    for j in range(0, ddls[len(ddls) - 1] + 1):
      t = min(j, ddls[i]) - times[i]
      if t < 0:
        schedule[i][j] = schedule[i-1][j]
      else:
        schedule[i][j] = max(schedule[i-1][j], 1 + schedule[i-1][t])

  print schedule
  print ""
  print_schedule(len(ddls) - 1, ddls[len(ddls) - 1], schedule, times, ddls)
  return

def print_schedule(i, j, schedule, times, ddls):
  print i, j
  if i < 0:
    return
  if schedule[i][j] == schedule[i - 1][j]:
    print_schedule(i - 1, j, schedule, times, ddls)
  else:
    t = min(j, ddls[i]) - times[i]
    print t
    print_schedule(i - 1, t, schedule, times, ddls)
    print "Schedule " + str(i) + " at time " + str(t)

if __name__ == "__main__":
  ddls = [1, 2, 3, 5]
  times = [1, 1, 3, 1]

  schedule_jobs(ddls, times)