import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.path import Path
import matplotlib.patches as patches


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

    A = np.zeros((COLUMNS, ROWS), dtype=int)
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


def plotMaze(A, path=[]):
    cmap = colors.ListedColormap(['white', 'black', 'green', 'red'])
    fig, ax = plt.subplots()
    ax.imshow(A, cmap=cmap)

    # Major ticks
    ax.set_xticks(np.arange(0, COLUMNS, 1))
    ax.set_yticks(np.arange(0, ROWS, 1))

    # Labels for major ticks
    # ax.set_xticklabels(np.arange(1, ROWS+1, 1))
    # ax.set_yticklabels(np.arange(1, COLUMNS + 1, 1))

    # Minor ticks
    ax.set_xticks(np.arange(-.5, COLUMNS, 1), minor=True)
    ax.set_yticks(np.arange(-.5, ROWS, 1), minor=True)
    ax.grid(which='minor', axis='both', linestyle='-', color='k', linewidth=2)
    ax.xaxis.tick_top()
    verts = [(t[1], t[0]) for t in path]

    codes = [Path.MOVETO] + [Path.LINETO] * (len(verts) - 1)
    print(codes)

    path = Path(verts, codes)

    patch = patches.PathPatch(path, facecolor='none', lw=2, edgecolor='yellow', zorder=3, )
    ax.add_patch(patch)

    # plt.savefig('out.png', bbox_inches='tight', dpi=300)
    plt.show()


class Node(object):
    def __init__(self, data, parents=None):
        self.data = data
        self.children = []
        self.parents = [parents]

    def add_child(self, obj):
        self.children.append(obj)

    def add_parent(self, obj):
        self.parents.append(obj)


def getValidStates(Array, currentPos):
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
    ROWS = len(Array)
    COLUMNS = len(Array[0])

    i, j = currentPos
    L = []

    if j != 0:  # LEFT : A[i][j-1]
        if Array[i][j - 1] != 1:  # Not a WALL cell
            L.append((i, j - 1))

    if i != 0:  # UP   : A[i-1][j]
        if Array[i - 1][j] != 1:  # Not a WALL cell
            L.append((i - 1, j))

    if j != COLUMNS - 1:  # RIGHT: A[i][j+1]
        if Array[i][j + 1] != 1:  # Not a WALL cell
            L.append((i, j + 1))

    if i != ROWS - 1:  # DOWN : A[i+1][j]
        if Array[i + 1][j] != 1:  # Not a WALL cell
            L.append((i + 1, j))
    return L


def DepthFirstSearch(array, start, finish):
    """
    Returns the path if exists. [START, ... , FINISH]\n
    If the path does not exist returns a empty list (len = 0)\n

    -Some notes for DFS
        * DFS does not guarantees that the solution will be optimal


    :type array: np.Array
    :type start: tuple
    :type finish: tuple
    :rtype: List
    """
    rootNode = Node(start)
    closedSet = set()
    searchFront = [rootNode]  # Βάλε την αρχική κατάσταση στο μέτωπο της αναζήτησης.
    finishNode = None
    while len(searchFront) != 0:  # Αν το μέτωπο της αναζήτησης είναι κενό τότε σταμάτησε.
        currentNode = searchFront.pop(0)
        if currentNode.data not in closedSet:  # Αν η κατάσταση ανήκει στο κλειστό σύνολο τότε πήγαινε στο while.

            if currentNode.data == finish:  # Αν η κατάσταση είναι μία από τις τελικές, τότε ανέφερε τη λύση
                # print("Found : ", currentNode.data)
                finishNode = currentNode
                break  # Αν θέλεις και άλλες λύσεις πήγαινε στο βήμα 2. Αλλιώς σταμάτησε.
            else:  # Εφάρμοσε τους τελεστές μετάβασης για να βρεις τις καταστάσεις-παιδιά.
                for item in getValidStates(array, currentNode.data):
                    child = Node(item, currentNode)
                    currentNode.add_child(child)
                    searchFront.insert(0, child)  # Βάλε τις καταστάσεις-παιδιά στην αρχή του μετώπου της αναζήτησης.
            closedSet.add(currentNode.data)  # Βάλε την κατάσταση-γονέα στο κλειστό σύνολο.
    # backtracking
    if finishNode is None:
        print("No Solution Found!")
        return []
    else:
        path = []
        print("The solution is : ")
        currentNode = finishNode
        while currentNode != rootNode:
            print("\t", currentNode.data)
            currentNode = currentNode.parents[0]


if __name__ == '__main__':
    A, START, FINISH = readImage2Array()
    ROWS = len(A)
    COLUMNS = len(A[0])
    plotMaze(A)
    Def
