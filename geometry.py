import math
def circle_area(r):
    return math.pi*(r**2)

def hypotenuse(side1, side2):
    return math.sqrt(side1**2 + side2**2)

def draw_square(size):
    sq = [['#' for x in range(size)] for z in range(size)]
    for row in sq:
        for i,c in enumerate(row):
            print(c, end="  ")
            if i == len(row)-1:
                print("\n",end='')
