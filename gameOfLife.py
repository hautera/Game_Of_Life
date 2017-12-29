import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys, argparse

ON = 255
OFF = 0
vals = [ON, OFF]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-size", dest="num", required = False)
    parser.add_argument("-mov-file", dest="movfile", required=False)
    parser.add_argument("-v", action='store_true')
    args = parser.parse_args()
    if args.num:
        size = int(args.num)
    else:
        size = 100

    verbose = args.v

    grid = np.random.choice(vals, size*size, p=[0.2, 0.8]).reshape(size, size)
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, step, fargs=(img, grid, size, verbose), frames=1000, interval = 50 )
    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])
    plt.show()


def step( frameNum, img, grid, size, v ):
    newGrid = []
    if v and frameNum % 10 == 0:
        print("Up to frameNum = " + str(frameNum))
        
    for i in range(size):
        newGrid.append( [] )
        for j in range(size):
            total = int( (grid[i, (j + 1)%size] + grid[ i , (j - 1) % size ] + grid[ (i + 1) % size, j] + grid[ (i - 1) % size, j ] + grid[ (i + 1) % size, (j - 1) % size ] + grid[ (i - 1) % size, (j - 1) % size ] + grid[ (i + 1) % size, (j + 1) % size ] + grid[ (i - 1) % size, (j + 1) % size ]) / 255 )
            if( grid[i , j] == ON ):
                if( total < 2 or total > 3 ):
                    newGrid[i].append( OFF )
                else:
                    newGrid[i].append( ON )
            elif total == 3:
                newGrid[i].append( ON )
            else:
                newGrid[i].append( OFF )
    grid[:] = newGrid[:]
    img.set_data(newGrid)
    return img,

def verbose():
    print("Verbose mode")

if __name__ == '__main__':
    main()
