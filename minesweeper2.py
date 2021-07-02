#python logic using 2d matrix
import random
from typing import Counter


colomns = int(input("how many colomns?\n"))
rows = int(input("how many row?\n"))
mines = int(input("how many mines ?\n"))

boardInit = [['?' for i in range(colomns)] for j in range(rows)]
boardMines = [['?' for i in range(colomns)] for j in range(rows)]


def drawBoardInit():
    for r in boardInit:
            for c in r:
                print(c,end = " ")
            print()

def drawBoardMines():
    for r in boardMines:
            for c in r:
                print(c,end = " ")
            print()

def generateMines():
    for x in range(mines):
        Xposition = random.randint(0,len(boardInit)-1)
        Yposition = random.randint(0,len(boardInit[0])-1)
        boardMines[Xposition][Yposition] = "M"

def mineDetection():
    # _______
    # |_|_|_|
    # |_|I|_|
    # |_|_|_|

    # # from i we will move up one spot moveing clockwise till we touch the spot above again

    #looping through 2d array
    for j in range(colomns):
        for i in range(rows):
            print(boardMines[i][j])
            if boardMines[i][j] == "?":
                try:
                    Counter = 0
                    if (boardMines[i-1][j] == "M"): #:above the i
                        Counter += 1
                    if (boardMines[i-1][j+1] == "M"): # top right of i
                        Counter += 1
                    if (boardMines[i][j+1] == "M"): #: right of i
                        Counter += 1
                    if (boardMines[i+1][j+1] == "M"): # bottom right of i
                        Counter += 1
                    if (boardMines[i+1][j] == "M"): #bottom of i
                        Counter += 1
                    if (boardMines[i+1][j-1] == "M"): # bottom left of i
                        Counter += 1
                    if (boardMines[i][j-1] == "M"): # left of i
                        Counter += 1
                    if (boardMines[i-1][j-1] == "M"): # top left of i
                        Counter += 1

                    boardMines[i][j] = Counter
                except:
                    print("index out of bounds")

    # for y in range(len(boardMines)+1):
    #     for x in range(len(boardMines[y])):
    #         print(y,x, boardMines[y][x])
    #         if boardMines[x][y] == "?":
    #             try:
                    

    #                 
    #                 if x == len(boardMines) and y == len(boardMines):
    #                     pass 
    #             except:
    #                 print("idk throwing me an error")    



def userin():
    #oorf = open or flag
    error = True
    while error == True: 
        oorf = input("open, flag or unflag a point\n")
        if(oorf == "open"):
            error2 = True
            while error2 == True:
                pointx = int(input("y axis of point to open\n"))
                pointy = int(input("x axis of point to open\n"))
                error = False
                if(pointx <= -1 or pointy <= -1 or pointx >=len(boardInit) or pointy >= len(boardInit)):
                    error2 = True
                else:
                    if boardMines[pointy][pointx] == "M":
                        print("You Struck a mine :(")
                        print("GAME OVER!")
                        boardInit[pointy][pointx] == "M"
                        for r in boardMines:
                            for c in r:
                                print(c,end = " ")
                            print()
                        break
                
                    if boardInit[pointy][pointx] == "F":
                        print("Point is flagged!")
                        print("please unflag point")

                    if boardMines[pointy][pointx] == "?":
                        Counter = 0
                        print(boardMines[pointy-1][pointx]) #above the i
                        print(boardMines[pointy-1][pointx+1]) # top right of i
                        print(boardMines[pointy][pointx+1]) # right of i
                        print(boardMines[pointy+1][pointx+1]) # bottom right of i
                        print(boardMines[pointy+1][pointx]) # bottom of i
                        print(boardMines[pointy+1][pointx-1]) # bottom left of i
                        print(boardMines[pointy][pointx-1]) # left of i
                        print(boardMines[pointy-1][pointx-1]) # top left of i

                        if (boardMines[pointy-1][pointx] == "M"): #:above the i
                            Counter += 1
                        if (boardMines[pointy-1][pointx+1] == "M"): # top right of i
                            Counter += 1
                        if (boardMines[pointy][pointx+1] == "M"): #: right of i
                            Counter += 1
                        if (boardMines[pointy+1][pointx+1] == "M"): # bottom right of i
                            Counter += 1
                        if (boardMines[pointy+1][pointx] == "M"): #bottom of i
                            Counter += 1
                        if (boardMines[pointy+1][pointx-1] == "M"): # bottom left of i
                            Counter += 1
                        if (boardMines[pointy][pointx-1] == "M"): # left of i
                            Counter += 1
                        if (boardMines[pointy-1][pointx-1] == "M"): # top left of i
                            Counter += 1

                        boardMines[pointx][pointy] = Counter
                        boardInit[pointx][pointy] = Counter
                        #boardInit[pointy][pointx] = " "    
                    error2 = False
            
        elif(oorf == "flag"):
            error2 = True
            while error2 == True:

                pointx = int(input("y axis of point to flag\n"))
                pointy = int(input("x axis of point to flag\n"))

                if(pointx <= -1 or pointy <= -1 or pointx >=len(boardInit) or pointy >= len(boardInit)):
                    error2 = True
                else:    
                    boardInit[pointy][pointx] = "F"
                    error2 = False

                error = False

        elif(oorf == "unflag"):
            error2 = True
            while error2 == True:
                pointx = int(input("y axis of point to unflag\n"))
                pointy = int(input("x axis of point to unflag\n"))

                if(pointx <= -1 or pointy <= -1 or pointx >=len(boardInit) or pointy >= len(boardInit)):
                    error2 = True
                else:
                    if boardInit[pointy][pointx] == "F":
                        boardInit[pointy][pointx] == "?"
                    if boardInit[pointy][pointx] != "F":
                        print("There is no flag there")
                    error2 = False
                error = False
        
        elif(oorf == "cheats"):
            for r in boardMines:
                for c in r:
                    print(c,end = " ")
                print()

        else:
            ("please input open, flag or unflag")
            error = True

def main():
    while True:
        drawBoardInit()
        generateMines()
        mineDetection()
        #drawBoardMines()
        userin()

if __name__ == "__main__":
    main()
 