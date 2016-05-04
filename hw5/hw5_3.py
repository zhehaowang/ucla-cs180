import os, sys

def string_cut(input_str, cut_array):
  
  cnt = 1
  cut_points = [0]
  for i in cut_array:
    if i == 1:
      cut_points.append(cnt)
    cnt += 1
  cut_points.append(len(input_str))
  print(cut_points)

  cut_points_cnt = len(cut_points)

  cost = [[0 for x in range(cut_points_cnt)] for y in range(cut_points_cnt)] 
  result = [[0 for x in range(cut_points_cnt)] for y in range(cut_points_cnt)] 

  for i in range(2, cut_points_cnt):
    for j in range(0, cut_points_cnt - i):
      cost[j][j+i] = cut_points[j+i] - cut_points[j]
      print "cost(" + str(j) + "," + str(j+i) + ") : " + str(cost[j][j+i])

      lower = 100
      index = 0
      for k in range(1, i):
        print str(j) + "," + str(j+k) + "," + str(j+i) + " : " + str(cost[j][j+k] + cost[j+k][j+i])
        if cost[j][j+k] + cost[j+k][j+i] < lower:
          index = j+k
          lower = cost[j][j+k] + cost[j+k][j+i]
      cost[j][j+i] += lower
      result[j][j+i] = index
      print "updated with cut: " + str(j) + "," + str(j+i) + " : " + str(cost[j][j+i])

  print(cost)
  print(result)
  print_cut_point(cut_points, result, 0, cut_points_cnt - 1)

  return

def print_cut_point(cut_points, matrix, start, end):
  temp = matrix[start][end]
  #print start, end, temp
  if cut_points[temp] != 0:
    print cut_points[temp]
  if temp == 0:
    return
  print_cut_point(cut_points, matrix, start, temp)
  print_cut_point(cut_points, matrix, temp, end)
  return

if __name__ == "__main__":
  input_str = "string_st"
  cut_array = [1,0,1,0,1,0,1,1]

  #input_str = "string"
  #cut_array = [1,0,1,0,1]

  string_cut(input_str, cut_array)