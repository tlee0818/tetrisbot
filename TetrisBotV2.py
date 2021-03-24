import copy
import PIL
import PIL.ImageGrab
from pynput import mouse
from pynput.keyboard import Key, Controller
import time

def initMoveDict():
    moveDict = {}

    #O Piece
    moveDict[("OPiece", 0, 0)] = ["DASL", "D"]
    moveDict[("OPiece", 0, 1)] = ["DASL", "R", "D"]
    moveDict[("OPiece", 0, 2)] = ['L', 'L', 'D']
    moveDict[("OPiece", 0, 3)] = ['L', 'D']
    moveDict[("OPiece", 0, 4)] = ['D']
    moveDict[("OPiece", 0, 5)] = ['R', 'D']
    moveDict[("OPiece", 0, 6)] = ['R', 'R', 'D']
    moveDict[("OPiece", 0, 7)] = ['DASR', 'L', 'D']
    moveDict[("OPiece", 0, 8)] = ['DASR', 'D']

    #T Piece
    moveDict[("TPiece", 0, 0)] = ['DASL', 'D']
    moveDict[("TPiece", 0, 1)] = ['L','L','D']
    moveDict[("TPiece", 0, 2)] = ['L','D']
    moveDict[("TPiece", 0, 3)] = ['D']
    moveDict[("TPiece", 0, 4)] = ['R','D']
    moveDict[("TPiece", 0, 5)] = ['R','R','D']
    moveDict[("TPiece", 0, 6)] = ['DASR','L','D']
    moveDict[("TPiece", 0, 7)] = ['DASR', 'D']
    moveDict[("TPiece", 1, 0)] = ['CW', 'DASL','D']
    moveDict[("TPiece", 1, 1)] = ['DASL', 'CW', 'D']
    moveDict[("TPiece", 1, 2)] = ['CW','L','L','D']
    moveDict[("TPiece", 1, 3)] = ['CW', 'L', 'D']
    moveDict[("TPiece", 1, 4)] = ['CW', 'D']
    moveDict[("TPiece", 1, 5)] = ['CW', 'R', 'D']
    moveDict[("TPiece", 1, 6)] = ['CW','R','R','D']
    moveDict[("TPiece", 1, 7)] = ['CW','DASR','L','D']
    moveDict[("TPiece", 1, 8)] = ['DASR','CW','D']
    moveDict[("TPiece", 2, 0)] = ['DASL', 'CW','CW','D']
    moveDict[("TPiece", 2, 1)] = ['L','L','CW','CW','D']
    moveDict[("TPiece", 2, 2)] = ['L','CW','CW','D']
    moveDict[("TPiece", 2, 3)] = ['CW','CW','D']
    moveDict[("TPiece", 2, 4)] = ['R','CW','CW','D']
    moveDict[("TPiece", 2, 5)] = ['R','R','CW','CW','D']
    moveDict[("TPiece", 2, 6)] = ['DASR','L','CW','CW','D']
    moveDict[("TPiece", 2, 7)] = ['DASR','CW','CW','D']
    moveDict[("TPiece", 3, 0)] = ['CCW','DASL','D']
    moveDict[("TPiece", 3, 1)] = ['CCW','L','L','D']
    moveDict[("TPiece", 3, 2)] = ['CCW','L','D']
    moveDict[("TPiece", 3, 3)] = ['CCW','D']
    moveDict[("TPiece", 3, 4)] = ['CCW','R','D']
    moveDict[("TPiece", 3, 5)] = ['CCW','R','R','D']
    moveDict[("TPiece", 3, 6)] = ['DASR','L','CCW','D']
    moveDict[("TPiece", 3, 7)] = ['DASR','CCW','D']
    moveDict[("TPiece", 3, 8)] = ['CCW','DASR','D']

    #L Piece
    moveDict[("LPiece", 0, 0)] = ['DASL','D']
    moveDict[("LPiece", 0, 1)] = ['L','L','D']
    moveDict[("LPiece", 0, 2)] = ['L','D']
    moveDict[("LPiece", 0, 3)] = ['D']
    moveDict[("LPiece", 0, 4)] = ['R','D']
    moveDict[("LPiece", 0, 5)] = ['R','R','D']
    moveDict[("LPiece", 0, 6)] = ['DASR','L','D']
    moveDict[("LPiece", 0, 7)] = ['DASR','D']
    moveDict[("LPiece", 1, 0)] = ['CW','DASL','D']
    moveDict[("LPiece", 1, 1)] = ['DASL', 'CW', 'D']
    moveDict[("LPiece", 1, 2)] = ['CW', 'L', 'L', 'D']
    moveDict[("LPiece", 1, 3)] = ['CW', 'L', 'D']
    moveDict[("LPiece", 1, 4)] = ['CW', 'D']
    moveDict[("LPiece", 1, 5)] = ['CW', 'R', 'D']
    moveDict[("LPiece", 1, 6)] = ['CW', 'R', 'R', 'D']
    moveDict[("LPiece", 1, 7)] = ['CW', 'DASR', 'L', 'D']
    moveDict[("LPiece", 1, 8)] = ['DASR', 'CW', 'D']
    moveDict[("LPiece", 2, 0)] = ['DASL', 'CW', 'CW', 'D']
    moveDict[("LPiece", 2, 1)] = ['L', 'L', 'CW', 'CW', 'D']
    moveDict[("LPiece", 2, 2)] = ['L', 'CW', 'CW', 'D']
    moveDict[("LPiece", 2, 3)] = ['CW', 'CW', 'D']
    moveDict[("LPiece", 2, 4)] = ['R', 'CW', 'CW', 'D']
    moveDict[("LPiece", 2, 5)] = ['R', 'R', 'CW', 'CW', 'D']
    moveDict[("LPiece", 2, 6)] = ['DASR', 'L', 'CW', 'CW', 'D']
    moveDict[("LPiece", 2, 7)] = ['DASR', 'CW', 'CW', 'D']
    moveDict[("LPiece", 3, 0)] = ['CCW', 'DASL', 'D']
    moveDict[("LPiece", 3, 1)] = ['CCW', 'L', 'L', 'D']
    moveDict[("LPiece", 3, 2)] = [ 'CCW', 'L', 'D']
    moveDict[("LPiece", 3, 3)] = ['CCW', 'D']
    moveDict[("LPiece", 3, 4)] = ['CCW', 'R', 'D']
    moveDict[("LPiece", 3, 5)] = ['CCW', 'R', 'R', 'D']
    moveDict[("LPiece", 3, 6)] = ['DASR', 'L', 'CCW', 'D']
    moveDict[("LPiece", 3, 7)] = ['DASR', 'CCW', 'D']
    moveDict[("LPiece", 3, 8)] = ['CCW', 'DASR', 'D']

    #J Piece
    moveDict[("JPiece", 0, 0)] = ['DASL', 'D']
    moveDict[("JPiece", 0, 1)] = ['L', 'L', 'D']
    moveDict[("JPiece", 0, 2)] = ['L', 'D']
    moveDict[("JPiece", 0, 3)] = ['D']
    moveDict[("JPiece", 0, 4)] = ['R', 'D']
    moveDict[("JPiece", 0, 5)] = ['R', 'R', 'D']
    moveDict[("JPiece", 0, 6)] = ['DASR', 'L', 'D']
    moveDict[("JPiece", 0, 7)] = ['DASR', 'D']
    moveDict[("JPiece", 1, 0)] = ['CW', 'DASL', 'D']
    moveDict[("JPiece", 1, 1)] = ['DASL', 'CW', 'D']
    moveDict[("JPiece", 1, 2)] = ['CW', 'L', 'L', 'D']
    moveDict[("JPiece", 1, 3)] = ['CW', 'L', 'D']
    moveDict[("JPiece", 1, 4)] = ['CW', 'D']
    moveDict[("JPiece", 1, 5)] = ['CW', 'R', 'D']
    moveDict[("JPiece", 1, 6)] = ['CW', 'R', 'R', 'D']
    moveDict[("JPiece", 1, 7)] = ['CW', 'DASR', 'L', 'D']
    moveDict[("JPiece", 1, 8)] = ['DASR', 'CW', 'D']
    moveDict[("JPiece", 2, 0)] = ['DASL', 'CW', 'CW', 'D']
    moveDict[("JPiece", 2, 1)] = ['L', 'L', 'CW', 'CW', 'D']
    moveDict[("JPiece", 2, 2)] = ['L', 'CW', 'CW', 'D']
    moveDict[("JPiece", 2, 3)] = ['CW', 'CW', 'D']
    moveDict[("JPiece", 2, 4)] = ['R', 'CW', 'CW', 'D']
    moveDict[("JPiece", 2, 5)] = ['R', 'R', 'CW', 'CW', 'D']
    moveDict[("JPiece", 2, 6)] = ['DASR', 'L', 'CW', 'CW', 'D']
    moveDict[("JPiece", 2, 7)] = ['DASR', 'CW', 'CW', 'D']
    moveDict[("JPiece", 3, 0)] = ['CCW', 'DASL', 'D']
    moveDict[("JPiece", 3, 1)] = ['CCW', 'L', 'L', 'D']
    moveDict[("JPiece", 3, 2)] = ['CCW', 'L', 'D']
    moveDict[("JPiece", 3, 3)] = ['CCW', 'D']
    moveDict[("JPiece", 3, 4)] = ['CCW', 'R', 'D']
    moveDict[("JPiece", 3, 5)] = ['CCW', 'R', 'R', 'D']
    moveDict[("JPiece", 3, 6)] = ['DASR', 'L', 'CCW', 'D']
    moveDict[("JPiece", 3, 7)] = ['DASR', 'CCW', 'D']
    moveDict[("JPiece", 3, 8)] = ['CCW', 'DASR', 'D']

    #S Piece
    moveDict[("SPiece", 0, 0)] = ['DASL', 'D']
    moveDict[("SPiece", 0, 1)] = ['L', 'L', 'D']
    moveDict[("SPiece", 0, 2)] = ['L', 'D']
    moveDict[("SPiece", 0, 3)] = ['D']
    moveDict[("SPiece", 0, 4)] = ['R', 'D']
    moveDict[("SPiece", 0, 5)] = ['R', 'R', 'D']
    moveDict[("SPiece", 0, 6)] = ['DASR', 'L', 'D']
    moveDict[("SPiece", 0, 7)] = ['DASR', 'D']
    moveDict[("SPiece", 1, 0)] = ['CCW', 'DASL', 'D']
    moveDict[("SPiece", 1, 1)] = ['DASL', 'CW', 'D']
    moveDict[("SPiece", 1, 2)] = ['CCW', 'L', 'D']
    moveDict[("SPiece", 1, 3)] = ['CCW', 'D']
    moveDict[("SPiece", 1, 4)] = ['CW', 'D']
    moveDict[("SPiece", 1, 5)] = ['CW', 'R', 'D']
    moveDict[("SPiece", 1, 6)] = ['CW', 'R', 'R', 'D']
    moveDict[("SPiece", 1, 7)] = ['DASR', 'CCW', 'D']
    moveDict[("SPiece", 1, 8)] = ['CW', 'DASR', 'D']

    #Z Piece
    moveDict[("ZPiece", 0, 0)] = ['DASL', 'D']
    moveDict[("ZPiece", 0, 1)] = ['L',  'L', 'D']
    moveDict[("ZPiece", 0, 2)] = ['L', 'D']
    moveDict[("ZPiece", 0, 3)] = ['D']
    moveDict[("ZPiece", 0, 4)] = ['R', 'D']
    moveDict[("ZPiece", 0, 5)] = ['R', 'R', 'D']
    moveDict[("ZPiece", 0, 6)] = ['DASR', 'L', 'D']
    moveDict[("ZPiece", 0, 7)] = ['DASR', 'D']
    moveDict[("ZPiece", 1, 0)] = ['CCW', 'DASL', 'D']
    moveDict[("ZPiece", 1, 1)] = ['DASL', 'CW', 'D']
    moveDict[("ZPiece", 1, 2)] = ['CCW', 'L', 'D']
    moveDict[("ZPiece", 1, 3)] = ['CCW', 'D']
    moveDict[("ZPiece", 1, 4)] = ['CW', 'D']
    moveDict[("ZPiece", 1, 5)] = ['CW', 'R', 'D']
    moveDict[("ZPiece", 1, 6)] = ['CW', 'R', 'R', 'D']
    moveDict[("ZPiece", 1, 7)] = ['DASR', 'CCW', 'D']
    moveDict[("ZPiece", 1, 8)] = ['CW', 'DASR', 'D']

    #I Piece
    moveDict[("IPiece", 0, 0)] = ['DASL','D']
    moveDict[("IPiece", 0, 1)] = ['L','L','D']
    moveDict[("IPiece", 0, 2)] = ['L','D']
    moveDict[("IPiece", 0, 3)] = ['D']
    moveDict[("IPiece", 0, 4)] = ['R','D']
    moveDict[("IPiece", 0, 5)] = ['R','R','D']
    moveDict[("IPiece", 0, 6)] = ['DASR','D']
    moveDict[("IPiece", 1, 0)] = ['CCW','DASL','D']
    moveDict[("IPiece", 1, 1)] = ['DASL', 'CCW','D']
    moveDict[("IPiece", 1, 2)] = ['DASL','CW','D']
    moveDict[("IPiece", 1, 3)] = ['L','CCW','D']
    moveDict[("IPiece", 1, 4)] = ['CCW','D']
    moveDict[("IPiece", 1, 5)] = ['CW','D']
    moveDict[("IPiece", 1, 6)] = ['R','CW','D']
    moveDict[("IPiece", 1, 7)] = ['DASR','CCW','D']
    moveDict[("IPiece", 1, 8)] = ['DASR','CW','D']
    moveDict[("IPiece", 1, 9)] = ['CW','DASR','D']
    
    return moveDict

moveWait = .03
dropWait = .2

def moveLeft(keyboard):
    keyboard.press(Key.left)
    time.sleep(moveWait)
    keyboard.release(Key.left)
    time.sleep(moveWait)
    
def moveRight(keyboard):
    keyboard.press(Key.right)
    time.sleep(moveWait)
    keyboard.release(Key.right)
    time.sleep(moveWait)
    
def DASLeft(keyboard):
    keyboard.press(Key.left)
    time.sleep(moveWait)
    keyboard.release(Key.left)
    time.sleep(moveWait)
    keyboard.press(Key.left)
    time.sleep(moveWait)
    keyboard.release(Key.left)
    time.sleep(moveWait)
    keyboard.press(Key.left)
    time.sleep(moveWait)
    keyboard.release(Key.left)
    time.sleep(moveWait)
    keyboard.press(Key.left)
    time.sleep(moveWait)
    keyboard.release(Key.left)
    time.sleep(moveWait)
    keyboard.press(Key.left)
    time.sleep(moveWait)
    keyboard.release(Key.left)
    time.sleep(moveWait)
    
def DASRight(keyboard):
    keyboard.press(Key.right)
    time.sleep(moveWait)
    keyboard.release(Key.right)
    time.sleep(moveWait)
    keyboard.press(Key.right)
    time.sleep(moveWait)
    keyboard.release(Key.right)
    time.sleep(moveWait)
    keyboard.press(Key.right)
    time.sleep(moveWait)
    keyboard.release(Key.right)
    time.sleep(moveWait)
    keyboard.press(Key.right)
    time.sleep(moveWait)
    keyboard.release(Key.right)
    time.sleep(moveWait)
    keyboard.press(Key.right)
    time.sleep(moveWait)
    keyboard.release(Key.right)
    time.sleep(moveWait)
    keyboard.press(Key.right)
    time.sleep(moveWait)
    keyboard.release(Key.right)
    time.sleep(moveWait)

def rotateClockwise(keyboard):
    keyboard.press("x")
    time.sleep(moveWait)
    keyboard.release("x")
    time.sleep(moveWait)
    
def rotateCounterClockwise(keyboard):
    keyboard.press("z")
    time.sleep(moveWait)
    keyboard.release("z")
    time.sleep(moveWait)
    
def drop(keyboard):
    keyboard.press(Key.space)
    time.sleep(moveWait)
    keyboard.release(Key.space)
    time.sleep(dropWait)
    
def movePiece(bestMove, keyboard, moveDict):
    block = bestMove[0]
    if block in ("SPiece","ZPiece","IPiece"):
        rotation = bestMove[1] % 2
    else:
        rotation = bestMove[1]
        
    bestMove = (block, rotation, bestMove[2])
    moveList = moveDict[bestMove]
    
    for move in moveList:
        if move == "L":
            moveLeft(keyboard)
        elif move == "R":
            moveRight(keyboard)
        elif move == "CW":
            rotateClockwise(keyboard)
        elif move == "CCW":
            rotateCounterClockwise(keyboard)
        elif move == "DASL":
            DASLeft(keyboard)
        elif move == "DASR":
            DASRight(keyboard)
        elif move == "D":
            drop(keyboard)
        else:
            print("TYPO FOUND!")

def maxItemLength(a):
    maxLen = 0
    rows = len(a)
    cols = len(a[0])
    for row in range(rows):
        for col in range(cols):
            maxLen = max(maxLen, len(str(a[row][col])))
    return maxLen

def print2dList(a):
    if (a == []):
        # So we don't crash accessing a[0]
        print([])
        return
    rows = len(a)
    cols = len(a[0])
    fieldWidth = maxItemLength(a)
    print("[ ", end="")
    for row in range(rows):
        if (row > 0): print("\n  ", end="")
        print("[ ", end="")
        for col in range(cols):
            if (col > 0): print(", ", end="")
            # The next 2 lines print a[row][col] with the given fieldWidth
            formatSpec = "%" + str(fieldWidth) + "s"
            print(formatSpec % str(a[row][col]), end="")
        print(" ]", end="")
    print("]") 
    
def getHoles(gameState):
    holes = 0
    holeCount = {}
    for row in gameState[::-1]:
        for col in range(len(row)):
            if row[col] == 0:
                if col not in holeCount:
                    holeCount[col] = 0
                holeCount[col] += 1   
            elif col in holeCount: #1 and previously Col prev 0
                holes += holeCount[col]
                del holeCount[col]
    return holes
    
def getHeights(gameState):
    boardRows = len(gameState)
    heights = [0] * len(gameState[0])
    for rowCount, row in enumerate(gameState):
        for colCount, col in enumerate(row):
            if col == 1 and heights[colCount] == 0:
                heights[colCount] = boardRows - rowCount
    return heights
    
def getBumpiness(heights):
    bumps = 0
    for i in range(len(heights) - 1):
        bumps += abs(heights[i] - heights[i+1])
    return bumps

def getDeepHoles(l):
    count = 0
    for n in range(1, 9):
        res1 = l[n-1] - l[n]
        res2 = l[n+1] - l[n]
        if res1 > 2 and res2 > 2:
            count += 1
    return count
    
def evaluateBoard(gameState, linesCleared):
    holeWeight = -6
    heightWeight = -5
    linesClearedWeight = 1
    bumpinessWeight = -.5
    wellWeight = -10
    dangerWeight = -1000
    
    heights = getHeights(gameState)
    
    danger = inDanger(gameState) * dangerWeight
    heightScore = sum(heights) * heightWeight
    holes = getHoles(gameState) * holeWeight
    wells = getDeepHoles(heights) * wellWeight
    bumpiness = getBumpiness(heights) * bumpinessWeight
    cleared = linesCleared * linesClearedWeight
    
    return holes + heightScore + bumpiness + cleared + wells + danger
     
def inDanger(gameState):
    row = gameState[1]
    if 1 in row:
        return True
    return False
    
#Returns (Piece, Rotation, Position)
def tetrisMinimax(gameStateDict):
    resultsDict = {}
    for key in gameStateDict:
        gameStates = gameStateDict[key]
        for position, gameState in enumerate(gameStates):
            gameState, linesCleared = clearLines(gameState)
            boardScore = evaluateBoard(gameState, linesCleared)
            resultsDict[boardScore] = (key[0], key[1], position)
    bestMove = max(resultsDict)
    return resultsDict[bestMove]
    
def clearLines(gameboard):
    
    count = 0
    newLine = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for r in range(len(gameboard) -1, -1, -1):
        if 0 not in gameboard[r]:
            nl  = copy.copy(newLine)
            gameboard.pop()
            gameboard.insert(0, nl)
            count += 1
            
    return (gameboard, count)
    
def possibleMoves(gameboard, piece):
    
    result = []
    
    tops = getHeights(gameboard)
    
    for c in range(len(gameboard[0]) - len(piece[0])+1):
        gb = copy.deepcopy(gameboard)

        coors = getCoordinates(gameboard, piece, c)
            
        for row in range(len(piece)):
            if row + coors[0] < 0:
                continue
            for col in range(len(piece[0])):
                gbR = row + coors[0]
                gbC = col + coors[1]
                if piece[row][col] == 1:
                    gb[gbR][gbC] = 1
        
        result.append(gb)
        
    return result
        
def getCoordinates(gameboard, piece, col):
    tops = getHeights(gameboard)
    result = []
    residuals = []
    residualResults = []
    
    for c in range(len(piece[0])):
        for r in range(len(piece)-1, -1, -1):
            if piece[r][c] == 1:
                n = r - len(piece) + 1
                residuals.append(r - len(piece) + 1)
                break
                

    for c in range(len(piece[0])):
        residualResults.append(tops[col] + residuals[c])
        col += 1
        
    a = max(residualResults)
    col -= len(piece[0])
    
    trR = len(gameboard) - a - len(piece)
    trC = col
    blR = len(gameboard) - a - 1
    blC = col + len(piece[0]) - 1 

    return (trR, trC)       

def getUserClick():
    clickedCoordinate = []
    def on_click(x, y, button, pressed):
        clickedCoordinate.append((x, y))
        if not pressed:
            # Stop listener
            return False
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    return clickedCoordinate[0]

def getBlockType(blockCoord):
    OPiece = ((239, 195, 15), [[1, 1],[1, 1]]) #
    TPiece = ((156, 90, 184), [[0, 1, 0],[1, 1, 1]]) #
    LPiece = ((230, 126, 35), [[0, 0, 1],[1, 1, 1]]) #
    JPiece = ((51, 151, 217),[[1, 0, 0],[1, 1, 1]]) #
    SPiece = ((156, 205, 56),[[0, 1, 1],[1, 1, 0]]) #
    ZPiece = ((230, 75, 60), [[1, 1, 0],[0, 1, 1]]) #
    IPiece = ((37, 187, 155),[[1, 1, 1, 1]]) #
    if blockCoord == OPiece[0]:
        return OPiece[1]
    elif blockCoord == TPiece[0]:
        return TPiece[1]
    elif blockCoord == LPiece[0]:
        return LPiece[1]
    elif blockCoord == SPiece[0]:
        return SPiece[1]
    elif blockCoord == ZPiece[0]:
        return ZPiece[1]
    elif blockCoord == JPiece[0]:
        return JPiece[1]
    elif blockCoord == IPiece[0]:
        return IPiece[1]
        
def getBlockTypeInStr(block):
    if block == [[1, 1],[1, 1]]:
        block = "OPiece"
    elif block == [[0, 1, 0],[1, 1, 1]]:
        block = "TPiece"
    elif block == [[0, 0, 1],[1, 1, 1]]:
        block = "LPiece"
    elif block == [[1, 0, 0],[1, 1, 1]]:
        block = "JPiece"
    elif block == [[0, 1, 1],[1, 1, 0]]:
        block = "SPiece"
    elif block == [[1, 1, 0],[0, 1, 1]]:
        block = "ZPiece"
    else:
        block = "IPiece"

def isBlock(color):
    if color[:3] == (0, 0, 0):
        return 0
    else:
        return 1
    
def getCurrentGameState(topLeft, bottomRight, nextBlockCoord):
    image = PIL.ImageGrab.grab()
    width = bottomRight[0] - topLeft[0]
    height = bottomRight[1] - topLeft[1]
    numRow, numCol = 20, 10
    gameState = []
    for row in range(numRow):
        gameState.append([])
        for col in range(numCol):
            x = int(topLeft[0] + width / numCol * (col+0.5))
            y = int(topLeft[1] + height / numRow * (row+0.5))
            color = image.load()[x, y]
            gameState[row].append(isBlock(color))
    
    blockColor = image.load()[nextBlockCoord[0], nextBlockCoord[1]]
    return gameState, getBlockType(blockColor)

def transpose2dList(lst):
    rows = len(lst)
    cols = len(lst[0])
    transposedLst = [[None] * rows for col in range(cols)]
    for row in range(rows):
        for col in range(cols):
            transposedLst[col][rows-row-1] = lst[row][col]
    return transposedLst

def getRotations(block):
    block = copy.deepcopy(block)
    numRows = len(block)
    numCols = len(block[0])
    # figures out number of possible rotations for block type
    if block == [[1,1],[1,1]]:
        return [block]
    else:
        numIterations = 4
    # finds all rotations, initialized with current rotation state
    allRotations = [block]
    for i in range(numIterations-1): # -1 b/c we already have 1 rotation
        transposedBlock = transpose2dList(block)
        allRotations.append(transposedBlock)
        block = transposedBlock
    return allRotations
    
def getAllGameStates(gameState, block):
    allRotations = getRotations(block)
    allGameStates = {}
    
    if block == [[1, 1],[1, 1]]:
        block = "OPiece"
    elif block == [[0, 1, 0],[1, 1, 1]]:
        block = "TPiece"
    elif block == [[0, 0, 1],[1, 1, 1]]:
        block = "LPiece"
    elif block == [[1, 0, 0],[1, 1, 1]]:
        block = "JPiece"
    elif block == [[0, 1, 1],[1, 1, 0]]:
        block = "SPiece"
    elif block == [[1, 1, 0],[0, 1, 1]]:
        block = "ZPiece"
    else:
        block = "IPiece"
        
    for r in range(len(allRotations)):
        possibleGameStates = possibleMoves(gameState, allRotations[r])
        allGameStates[(block, r)] = possibleGameStates
    return allGameStates

def testGetAllGameStates(gameState, block):
    for state in getAllGameStates(gameState, block):
        print2dList(state)

def restartGame(keyboard):
    keyboard.press("r")
    time.sleep(moveWait)
    keyboard.release("r")
    time.sleep(moveWait)
    
def getNextPiece(nextBlockCoord):
    x,y = nextBlockCoord
    blockColor =  PIL.ImageGrab.grab().load()[x,y]
    nextBlock = getBlockType(blockColor)
   
    return nextBlock
        
def run():
    print("Please click on the top left of the game screen")
    topLeft = getUserClick()
    print("Please click on the bottom right of the game screen")
    bottomRight = getUserClick()
    print("Please click on the location of the next piece")
    nextBlockCoord = getUserClick()
    
    #Initializing
    keyboard = Controller()
    moveDict = initMoveDict()
    
    #Start Game
    restartGame(keyboard)
    currPiece = getNextPiece(nextBlockCoord)
    heldPiece = None
    gameOver = False
    time.sleep(3)
    
    while not gameOver:
        gameState, nextPiece = getCurrentGameState(topLeft,
                                                bottomRight, nextBlockCoord)
                                                
        #Dictionary of All Poss Game States
        allPossGameStates = getAllGameStates(gameState, currPiece)
        bestMove = tetrisMinimax(allPossGameStates)
        movePiece(bestMove, keyboard, moveDict)
        
        currPiece = nextPiece 
    
run()