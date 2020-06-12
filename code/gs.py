
import sys
from random import randint

def get_neighbors(r, c, width, height):
    nighbors = []
    locations = ((r, c-1), (r, c+1),
                 (r-1, c-1), (r-1, c), (r-1, c+1),
                 (r+1, c-1), (r+1, c), (r+1, c+1))
    for row, col in locations:
        if ((row >= 0 and row < width)
                 and (col >= 0 and col < height)):
            nighbors.append((row, col))
    return nighbors

def get_local_min_delay_cell(r, c, t, A, D):
    locations = get_neighbors(r, c, len(A), len(A[0]))
    min_dely = 100 
    min_row = r
    min_col = c
    for row, col in locations:
        if A[row][col] == None:
            continue
        elif A[row][col] >= t:
            if D[row][col] < min_dely:
               min_dely = D[row][col]
               min_row = row
               min_col = col

    # is the current cell better than best neighbor
    if A[r][c] != None and A[r][c] >= t:
        if D[r][c] <= min_dely:
            return r, c
    return min_row, min_col

def get_min_delay_cell(t, A, D):
    # pick a random cell in the upper right triangle
    row_prev = randint(0, len(A) - 1)
    col_prev = randint(row_prev, len(A[0]) - 1)

    print('Starting at ({},{}): A={}, D={}'.format(row_prev, col_prev, A[row_prev][col_prev], D[row_prev][col_prev]))
    exhausted = False
    while not exhausted:
        row, col = get_local_min_delay_cell(row_prev, col_prev, t, A, D)
        if row == row_prev and col == col_prev:
            exhausted = True
        row_prev = row
        col_prev = col

    print('Finished at ({},{}): A={}, D={}'.format(row_prev, col_prev, A[row_prev][col_prev], D[row_prev][col_prev]))
    return row_prev, col_prev 


t = float(sys.argv[1]) if len(sys.argv) > 1 else 0.75

print('\n')
print('t={}'.format(t))

accuracy = [[0.793, 0.927, 0.977, 0.197, 0.145, 0.099, 0.33, 0.204, 0.305, 0.863], [None, 0.228, 0.288, 0.633, 0.501, 0.017, 0.164, 0.447, 0.283, 0.382], [None, None, 0.066, 0.302, 0.233, 0.649, 0.8, 0.697, 0.539, 0.75], [None, None, None, 0.683, 0.505, 0.228, 0.511, 0.157, 0.48, 0.503], [None, None, None, None, 0.854, 0.838, 0.152, 0.181, 0.103, 0.492], [None, None, None, None, None, 0.448, 0.569, 0.521, 0.238, 0.574], [None, None, None, None, None, None, 0.109, 0.984, 0.527, 0.093], [None, None, None, None, None, None, None, 0.261, 0.734, 0.425], [None, None, None, None, None, None, None, None, 0.229, 0.169], [None, None, None, None, None, None, None, None, None, 0.812]]


delay = [[0.983, 0.218, 0.421, 0.586, 0.276, 0.665, 0.643, 0.87, 0.399, 0.737], [None, 0.193, 0.002, 0.847, 0.517, 0.688, 0.853, 0.485, 0.258, 0.817], [None, None, 0.319, 0.199, 0.474, 0.198, 0.193, 0.924, 0.71, 0.205], [None, None, None, 0.208, 0.196, 0.723, 0.445, 0.327, 0.912, 0.463], [None, None, None, None, 0.778, 0.064, 0.483, 0.606, 0.988, 0.842], [None, None, None, None, None, 0.36, 0.214, 0.347, 0.205, 0.501], [None, None, None, None, None, None, 0.249, 0.117, 0.185, 0.874], [None, None, None, None, None, None, None, 0.14, 0.228, 0.36], [None, None, None, None, None, None, None, None, 0.565, 0.511], [None, None, None, None, None, None, None, None, None, 0.652]]

get_min_delay_cell(t, accuracy, delay)
print('\n')

# add axis labels
accuracy.insert(0, [x for x in range(len(accuracy))])
delay.insert(0, [x for x in range(len(delay))])

[accuracy[y].insert(0, y - 1) for y in range(len(accuracy))]
[delay[y].insert(0, y - 1) for y in range(len(delay))]

accuracy[0][0] = ''
delay[0][0] = ''

print('A:')
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in accuracy]))

print('\n\n')
print('D:')
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in delay]))
print('\n\n')


