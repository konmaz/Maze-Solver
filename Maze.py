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


if __name__ == '__main__':

    im = Image.open('in.png').convert('RGB')  # type: Image.Image
    ROWS, COLUMNS = im.size

    A = np.zeros((COLUMNS, ROWS))
    START = (0, 0)
    END = (0, 0)
    for i in range(ROWS):
        for j in range(COLUMNS):
            c = color(im.getpixel((i, j)))
            A[j][i] = c
            if c == 2:
                START = (j, i)
            if c == 3:
                END = (j, i)

    cmap = colors.ListedColormap(['white', 'black', 'green', 'red'])
    fig, ax = plt.subplots()

    ax.imshow(A, cmap=cmap)

    # Major ticks
    ax.set_xticks(np.arange(0, 10, 1))
    ax.set_yticks(np.arange(0, COLUMNS, 1))

    # Labels for major ticks
    ax.set_xticklabels(np.arange(1, 11, 1))
    ax.set_yticklabels(np.arange(1, COLUMNS+1, 1))

    # Minor ticks
    ax.set_xticks(np.arange(-.5, 10, 1), minor=True)
    ax.set_yticks(np.arange(-.5, COLUMNS, 1), minor=True)
    ax.grid(which='minor', axis='both', linestyle='-', color='k', linewidth=2)
    ax.xaxis.tick_top()
    plt.rcParams['figure.dpi'] = 300

    plt.show()
