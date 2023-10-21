#Complete inputed sudokus by elimination
import math

grid = [[0, 0, 1, 2, 0, 0, 8, 7, 0],
        [0, 0, 6, 0, 8, 0, 0, 2, 4],
        [0, 8, 0, 0, 7, 3, 0, 0, 5],
        [6, 2, 0, 1, 3, 0, 0, 8, 0],
        [8, 0, 0, 9, 4, 0, 0, 5, 2],
        [5, 9, 4, 0, 0, 8, 3, 0, 6],
        [3, 0, 9, 0, 0, 0, 5, 4, 0],
        [1, 0, 0, 0, 9, 0, 2, 0, 8],
        [0, 0, 0, 0, 5, 7, 0, 0, 0]]

grid_size = len(grid)
area_size = int(math.sqrt(grid_size))

def element_per_area(possible_values, row, column): #Eleminiate from the set "possible values" the numbers found in the current grid area
    for cell_row in range(row, row + area_size):
        for column_row in range(column, column + area_size):
            if isinstance(grid[cell_row][column_row], int):
               if grid[cell_row][column_row] in possible_values:
                possible_values.discard(grid[cell_row][column_row])

def element_per_row(possible_values, main_row): #Eleminiate from the set "possible values" the numbers found in the current row
    for row_element in range(grid_size):
        if isinstance(grid[main_row][row_element], int): 
          if grid[main_row][row_element] in possible_values:
              possible_values.discard(grid[main_row][row_element])

def element_per_column(possible_values, main_column): #Eleminiate from the set "possible values" the numbers found in the current column
    for i in range(grid_size):
      if isinstance(grid[i][main_column], int): 
        if grid[i][main_column] in possible_values:
            possible_values.discard(grid[i][main_column])

def solve_sudoku(row, column):
    for i in range(row, row + area_size): #Will analyse all empty grid elements per area and replace them with a value or a set with possible values
        for j in range(column, column + area_size):
            if grid[i][j] == 0:
                possible_values = {1, 2, 3, 4, 5, 6, 7, 8, 9}
                element_per_area(possible_values, row, column)
                element_per_row(possible_values, i)
                element_per_column(possible_values, j)
                
                if len(possible_values) == 1:
                    grid[i][j] = list(possible_values)[0]
                else:
                    grid[i][j] = possible_values

  
    for i in range(row, row + area_size): #Will go through all elements per area, the value is a set function are going to be called to lower the set of possible values to 1 and then replace it
      for j in range(column, column + area_size):
        if isinstance(grid[i][j], set) and len(grid[i][j]) > 1:
          possible_values = grid[i][j]
          element_per_area(possible_values, row, column)
          element_per_row(possible_values, i)
          element_per_column(possible_values, j)
          if len(possible_values) == 1:
            grid[i][j] = list(possible_values)[0]
          if grid[i][j] == 0:
            grid[i][j] = possible_values

for n in range(5): #Repeats the algorithm multiple times to garantee the completion of the sudoku
    for row in range(0, grid_size, area_size):  #Moves across the area of the grid and calls for the function "solve_sudoku" to analyse the grid elements from that current area
        for column in range(0, grid_size, area_size):
            solve_sudoku(row, column)

          

print("final grid:")
for r in grid:
    print(r)
