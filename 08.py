import sys
import os
from common import get_input

import math

example = '''30373
25512
65332
33549
35390
'''

def visible(forest, x, y):
    tree_height = forest[x][y]
    view_distance = [0, 0, 0, 0]

    # Scan Up
    for i in range(x - 1, -1, -1):
        view_distance[0] += 1
        if forest[i][y] >= tree_height:
            # Mark tree visible but blocking edge sight
            view_distance[0] -= 0.5
            break
    # Scan Left
    for i in range(y - 1, -1, -1):
        view_distance[1] += 1
        if forest[x][i] >= tree_height:
            # Mark tree visible but blocking edge sight
            view_distance[1] -= 0.5
            break
    # Scan Right
    for i in range(y + 1, len(forest[x])):
        view_distance[2] += 1
        if forest[x][i] >= tree_height:
            # Mark tree visible but blocking edge sight
            view_distance[2] -= 0.5
            break
    # Scan Down
    for i in range(x + 1, len(forest)):
        view_distance[3] += 1
        if forest[i][y] >= tree_height:
            # Mark tree visible but blocking edge sight
            view_distance[3] -= 0.5
            break
    
    return view_distance

def solution(data):
    # Calculate edge trees
    solution_1 = len(data)*2 + len(data[0])*2 - 4
    # Scenic score starts at 0
    solution_2 = 0
    # Loop through interior trees
    print(solution_1)
    for x in range(1, len(data[1:-1]) + 1):
        for y in range(1, len(data[x][1:-1]) + 1):
            # Calculate visibility
            view_distance = visible(data, x, y)
            if view_distance[0] == x:
                solution_1 += 1
            elif view_distance[1] == y:
                solution_1 += 1
            elif view_distance[2] == (len(data[x]) - y - 1):
                solution_1 += 1
            elif view_distance[3] == (len(data) - x - 1):
                solution_1 += 1
            
            # Calculate scenic score
            score = 1
            for i in view_distance:
                # Round up to include trees that stopped visibility
                score = score * math.ceil(i)
            if solution_2 < score:
                pass
                solution_2 = score

    return solution_1, solution_2

def parse_input(input):
    return [[int(y) for y in x] for x in input.splitlines()]

def main():
    test_data = parse_input(example)
    assert(visible(test_data, 3, 2) == [1.5, 2, 1.5, 1])
    solution_1, solution_2 = solution(test_data)
    assert(solution_1 == 21)
    assert(solution_2 == 8)

    program_file_name = sys.argv[0]
    input_file_name = 'input_' + os.path.splitext(program_file_name)[0] + '.txt'
    data = parse_input(get_input(input_file_name))
    solution_1, solution_2 = solution(data)
    print('Part 1: ', solution_1)
    assert(solution_1 == 1736)
    print('Part 2: ', solution_2)
    
if __name__ == '__main__':
    sys.exit(main())