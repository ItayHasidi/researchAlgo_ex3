import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: number of columns.
# h: number of rows.
line = []
w, h = [int(i) for i in input().split()]
for i in range(h):
    line.append([int(j) for j in input().split()])  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

print(line, file=sys.stderr, flush=True)


room_types = \
   [{'LEFT': (0, 0), 'TOP': (0, 0), 'RIGHT': (0, 0)},
    {'LEFT': (0, 1), 'TOP': (0, 1), 'RIGHT': (0, 1)},
    {'LEFT': (1, 0), 'TOP': (0, 0), 'RIGHT': (-1, 0)},
    {'LEFT': (0, 0), 'TOP': (0, 1), 'RIGHT': (0, 0)},
    {'LEFT': (0, 0), 'TOP': (-1, 0),'RIGHT': (0, 1)},
    {'LEFT': (0, 1), 'TOP': (1, 0), 'RIGHT': (0, 0)},
    {'LEFT': (1, 0), 'TOP': (0, 0), 'RIGHT': (-1, 0)},
    {'LEFT': (0, 0), 'TOP': (0, 1), 'RIGHT': (0, 1)},
    {'LEFT': (0, 1), 'TOP': (0, 0), 'RIGHT': (0, 1)},
    {'LEFT': (0, 1), 'TOP': (0, 1), 'RIGHT': (0, 0)},
    {'LEFT': (0, 0), 'TOP': (-1, 0),'RIGHT': (0, 0)},
    {'LEFT': (0, 0), 'TOP': (1, 0), 'RIGHT': (0, 0)},
    {'LEFT': (0, 0), 'TOP': (0, 0), 'RIGHT': (0, 1)},
    {'LEFT': (0, 1), 'TOP': (0, 0), 'RIGHT': (0, 0)}]

# game loop
while True:
    inputs = input().split()
    xi = int(inputs[0])
    yi = int(inputs[1])
    pos = inputs[2]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    dir = room_types[line[yi][xi]][pos]
    xi += dir[0]
    yi += dir[1]
    print(xi, yi)

    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    # print("0 0")
