# f(5, 5, 3, 3)

# // Should return:
# // [ 13, 8, 7, 12, 17, 18, 19,
# // 194, 9, 4, 3, 2, 1, 6,
# // 11, 16, 21, 22, 23, 24,
# // 25, 20, 15, 10, 5 ]

# f(2, 4, 1, 2) // [ 2, 1, 5, 6, 7, 3, 8, 4 ]

# Just blow it up and set the center point

def max_distance(rows, cols, row, col):
    return max(rows - row - 1, cols - col - 1)

def make_matrix(rows, cols, point):
    distance = max_distance(rows, cols, point[0], point[1])
    min_point = (point[0] - distance, point[1] - distance)
    max_point = (point[0] + distance, point[1] + distance)
    num = 1

    matrix = []

    for i in xrange(max_point[0] - min_point[0] + 1):
        c = max_point[1] - min_point[1] + 1
        matrix.append([0] * (c))
        for j in xrange(c):
            row = min_point[0] + i
            col = min_point[1] + j
            if 0 <= row < rows and 0 <= col < cols:
                matrix[i][j] = num
                num += 1
    return matrix


def traverse(matrix, start, end):
    if start == end:
        return [matrix[start[0]][start[1]]]

    down = [matrix[i][end[1]] for i in xrange(start[0], end[0] + 1) if matrix[i][end[1]] != 0]

    left = [matrix[end[0]][i] for i in xrange(start[1], end[1]) if matrix[end[0]][i] != 0]
    left.reverse()

    up = [matrix[i][start[1]] for i in xrange(start[0], end[0]) if matrix[i][start[1]] != 0]
    up.reverse()

    right = [matrix[start[0]][i] for i in xrange(start[1] + 1, end[1]) if matrix[start[0]][i] != 0]

    start = (start[0] + 1, start[1] + 1)
    end = (end[0] - 1, end[1] - 1)
    return down + left + up + right + traverse(matrix, start, end)

def f(rows, cols, row, col):
    matrix = make_matrix(rows, cols, (row - 1, col - 1))
    return list(reversed(traverse(matrix, (0, 0), [len(matrix) - 1] * 2)))


if __name__ == '__main__':
    print f(5, 5, 3, 3)
    print f(2, 4, 1, 2)