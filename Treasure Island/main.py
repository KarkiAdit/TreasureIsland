Island = IslandClass()

DisplayGrid()
for Treasure in range(3):
    Island.HideTreasure()

StartDig()
DisplayGrid()

class IslandClass:
 def __init__(self):
    Sand = '.'
    self.__Grid = [[Sand for j in range(30)]
    for i in range(10)]

def DisplayGrid() :
 for i in range (10) :
 for j in range (30) :
 print(island.GetSquare(i, j), end='')
 print()

def HideTreasure(self):
 Treasure = 'T'
 x = randint(0,9)
 y = randint(0,29)
 while self.__Grid[y][x] == Treasure:
 x = randint(0,9)
 y = randint(0,29)
 self.__Grid[y][x] = Treasure


def DigHole(self, x, y):
    Treasure = 'T'


Hole = 'O'

Foundtreasure = 'X'
if self.__Grid[x][y] == Treasure
self.__Grid[x][y] = Foundtreasure
else:
self.__Grid[x][y] = Hole
return

def StartDig() :
 Valid = False
 while not Valid : # validate down position
 try:
 x = int(input("position down <0 to 9> ? "))
 if x >= 0 and x <= 9 : 1
 Valid = True
 except:
 Valid = False
 Valid = False
 while not Valid : # validate across position
 try :
 y = int(input("position across <0 to 29> ? "))
 if y >= 0 and y <= 29
 Valid = True
 except :
 Valid = False
 island.DigHole(x, y)
 return