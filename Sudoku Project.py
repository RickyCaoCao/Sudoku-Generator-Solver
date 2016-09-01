#-------------------------------------------------------------------------------
# Name:        Sudoku Creator/Solver (using Backtracking)
# Purpose:
#
# Author:      Richard Cao
#
# Created:     31-08-2016
#
# Author's Note: The completed Sudoku Generator is made using a brute-force backtracking method.
# Part 2 - Dancing links are implemented in the form of Python dictionaries to "hollow"
# (or remove the givens from) the Sudoku
# Possible Optimizations:
# -Storing Rows, Columns, Boxes to Decrease Number of References (may increase memory usage)
#-------------------------------------------------------------------------------
import random

#Display Function
def DisplayGrid(grid):
    printGrid = [] #Initial List
    for i in range(9):
        if i in [3, 6]:
            for num in range(12):
                printGrid.append("-") #Creates the horizontal barriers
            printGrid.append("\n") #new line

        for j in range(9):
            if j in [3,6]:
                printGrid.append("|") #Vertical Barriers
            printGrid.append(str(grid[9*i + j].Value)) #Grabs number from a Sudoku grid and adds the item to the row
        printGrid.append("\n") #new line

    print("".join(printGrid))

##def GridArray(grid):
##    someGrid = []
##    for i in range(9):
##        row = []
##        for j in range(9):
##            row.append(grid[j].Value)
##        someGrid.append(row)
##    return someGrid

#----Part 1: Completed Sudoku Generator------------------------------------------------------
def CreateGrid():
    sudokuGrid = [] #Entire grid
    possibleNums = [] #Creates an array of possible numbers. Although memory-heavy, it is necessary for backtracking
    for i in range(81):
        aList = []
        for j in range(1, 10):
            aList.append(j) #Creates a list of numbers between 1 and 9, inclusive
        possibleNums.append(aList) #Adds the entire list


    num = 0 #number of iterations

    while num < 81:
        if len(possibleNums[num]) != 0:
            testIndex = GetRandomIndex(len(possibleNums[num]) - 1) #gets a random number between 0 and the length of the list (minus 1 to offset array indexing)
            testVal = possibleNums[num][testIndex] #retrieves a value

            if TestConflict(Square(num, testVal), sudokuGrid) == False:
                    sudokuGrid.append(Square(num, testVal))
                    del possibleNums[num][testIndex]
                    num += 1
            else:
                del possibleNums[num][testIndex]
        else:
            possibleNums[num] = []
            for i in range (1,10):
                possibleNums[num].append(i)
            num -= 1
            del sudokuGrid[num]

    DisplayGrid(sudokuGrid)

def GetRandomIndex(maxNum):
    return random.randint(0, maxNum)

def GetRow(anIndex):
    print(anIndex-1)
    return ((anIndex-1) // 9 + 1)

def GetColumn(anIndex):
    aNum = anIndex % 9
    if aNum == 0:
        return 9
    return(aNum)

def GetBox(row, col):
    if row >= 1 and row < 4 and col >= 1 and col < 4:
        return 1
    elif row >= 1 and row < 4 and col >= 4 and col < 7:
        return 2
    elif row >= 1 and row < 4 and col >= 7 and col < 10:
        return 3
    elif row >= 4 and row < 7 and col >= 1 and col < 4:
        return 4
    elif row >= 4 and row < 7 and col >= 4 and col < 7:
        return 5
    elif row >= 4 and row < 7 and col >= 7 and col < 10:
        return 6
    elif row >= 7 and row < 10 and col >= 1 and col < 4:
        return 7
    elif row >= 7 and row < 10 and col >= 4 and col < 7:
        return 8
    elif row >= 7 and row < 10 and col >= 7 and col < 10:
        return 9

class Square:
    def __init__(self, ind, val):
        ind += 1 #to accomodate indexing in lists
        self.Value = val
        self.Row = GetRow(ind)
        self.Column = GetColumn(ind)
        self.Box = GetBox(self.Row, self.Column)

def TestConflict(aSquare, grid):
    for item in grid:
        if item.Row == aSquare.Row or item.Column == aSquare.Column or item.Box == aSquare.Box:

            if item.Value == aSquare.Value:
                return True

    return False

#---Part 2: "Hollowing" the Puzzle ---------------------------------------------
#---Part 2a: Creating "Dancing Links" Solving Algorithm
#---Accredited to Ali Assaf (http://www.cs.mcgill.ca/~aassaf9/python/sudoku.txt)
#---http://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html----
#---http://garethrees.org/2007/06/10/zendoku-generation/---

#A dictionary is used to use Algorithm X.

def SolveSudoku(grid):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val:

def XSolve(universet, subsets):
    output = []
    if not universet: #when the set is empty
        yield output
    else:
        lowkey = min(universet, key=lambda lowkey: len(universet[lowkey]))  #from the universet, finds the key of the smallest list
        for item in universet[lowkey]:
            output.append(item)


#---Part 2b: Removing the Numbers Recursive Solution----------------------------
# Take 4 numbers at a time that are diagonally opposite, followed by 2 numbers at a time
#--------------Function---------------------------------------------------------
CreateGrid()
