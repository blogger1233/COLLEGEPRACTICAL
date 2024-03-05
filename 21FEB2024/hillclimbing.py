#aim : Aim: Wap to implement hill climbing.


import random
import numpy as np

coordinate = np.array([[1,2], [30,21], [56,23], [8,18], [20,50], [3,4], [11,6], [6,7], [15,20], [10,9], [12,12]])

def generate_matrix(coordinate):
   matrix = []
   for i in range(len(coordinate)):
       for j in range(len(coordinate)):
           p = np.linalg.norm(coordinate[i]-coordinate[j])
           matrix.append(p)
   matrix = np.reshape(matrix, (len(coordinate), len(coordinate)))
   return matrix

def solution(matrix):
   points = list(range(0, len(matrix)))
   solution = []
   for i in range(0,len(matrix)):
       random_point = points[random.randint(0, len(points)-1)]
       solution.append(random_point)
       points.remove(random_point)
   return solution

def path_length(matrix, solution):
   cycle_length = 0
   for i in range(0, len(solution)):
       cycle_length += matrix[solution[i]][solution[i-1]]
   return cycle_length

def neighbours(matrix, solution):
   neighbours = []
   for i in range(0, len(solution)):
       for j in range(i+1, len(solution)):
           neighbour = solution.copy()
           neighbour[i] = solution[j]
           neighbour[j] = solution[i]
           neighbours.append(neighbour)

   best_neighbour = neighbours[0]
   best_path = path_length(matrix, best_neighbour)

   for neighbour in neighbours:
       current_path = path_length(matrix, neighbour)
       if current_path < best_path:
           best_path = current_path
           best_neighbour = neighbour
   return best_neighbour, best_path

def hill_climbing(coordinate):
   matrix = generate_matrix(coordinate)
   current_solution = solution(matrix)
   current_path = path_length(matrix, current_solution)
   neighbour = neighbours(matrix, current_solution)[0]
   best_neighbour, best_neighbour_path = neighbours(matrix, neighbour)

   while best_neighbour_path < current_path:
       current_solution = best_neighbour
       current_path = best_neighbour_path
       neighbour = neighbours(matrix, current_solution)[0]
       best_neighbour, best_neighbour_path = neighbours(matrix, neighbour)

   return current_path, current_solution

final_solution = hill_climbing(coordinate)
print("The solution is \n", final_solution[1])
