import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import colors


def color(RGB) -> int:
    R, G, B = RGB
    if R == 255 and G == 255 and B == 255:
        return 0
    elif R == 0 and G == 0 and B == 0:
        return 1  # Wall
    elif R == 0 and G == 255 and B == 0:
        return 2  # Start
    elif R == 255 and G == 0 and B == 0:
        return 3  # Finish


def readImage2Array():
    im = Image.open('in.png').convert('RGB')  # type: Image.Image
    ROWS, COLUMNS = im.size

    A = np.zeros((COLUMNS, ROWS))
    start = (0, 0)
    finish = (0, 0)
    for i in range(ROWS):
        for j in range(COLUMNS):
            c = color(im.getpixel((i, j)))
            A[j][i] = c
            if c == 2:
                start = (j, i)
            if c == 3:
                finish = (j, i)
    return A, start, finish


def plotMaze():
    cmap = colors.ListedColormap(['white', 'black', 'green', 'red'])
    fig, ax = plt.subplots()
    ax.imshow(A, cmap=cmap)

    # Major ticks
    ax.set_xticks(np.arange(0, ROWS, 1))
    ax.set_yticks(np.arange(0, COLUMNS, 1))

    # Labels for major ticks
    # ax.set_xticklabels(np.arange(1, ROWS+1, 1))
    # ax.set_yticklabels(np.arange(1, COLUMNS + 1, 1))

    # Minor ticks
    ax.set_xticks(np.arange(-.5, ROWS, 1), minor=True)
    ax.set_yticks(np.arange(-.5, COLUMNS, 1), minor=True)
    ax.grid(which='minor', axis='both', linestyle='-', color='k', linewidth=2)
    ax.xaxis.tick_top()
    plt.savefig('out.png', bbox_inches='tight', dpi=300)
    # plt.show()


class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parents = []

    def add_child(self, obj):
        self.children.append(obj)

    def add_parent(self, obj):
        self.parents.append(obj)


def getValidStates(Array, currentPos: tuple):
    """
    A valid move is consider:
        UP   : A[i-1][j]
        DOWN : A[i+1][j]
        LEFT : A[i][j-1]
        RIGHT: A[i][j+1]

    but with the condition the cell isn't marked with 1 (WALL) or isn't out of bounds
    Returns a tuple int Array containing the possible Moves (Line,Collum)
    :rtype: tuple
    """
    i, j = currentPos
    L = []
    if i != 0:  # UP   : A[i-1][j]
        if A[i - 1][j] != 1:  # Not a WALL cell
            L.append(i - 1, j)

    if i != ROWS - 1:  # DOWN : A[i+1][j]
        if A[i + 1][j] != 1:  # Not a WALL cell
            L.append(i + 1, j)

    if j != 0:  # LEFT : A[i][j-1]
        if A[i][j - 1] != 1:  # Not a WALL cell
            L.append(i, j - 1)

    if j != COLUMNS - 1:  # RIGHT: A[i][j+1]
        if A[i][j + 1] != 1:  # Not a WALL cell
            L.append(i, j + 1)
    return L


def dfs():
    pass


if __name__ == '__main__':
    A, START, FINISH = readImage2Array()
    COLUMNS = len(A)
    ROWS = len(A[0])
    plotMaze()
    rootNode = Node(START)
    # getValidStates(0)