import sys
import os
from common import get_input

example = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''

def solution(data):
    head = [0, 0]
    tail = [0, 0]
    visited = set()
    
    for move in data:
        # Number of moves
        for i in range(move[1]):
            # Up
            if move[0] == 'U':
                head[0] += 1
            # Left
            if move[0] == 'L':
                head[1] -= 1
            # Right
            if move[0] == 'R':
                head[1] += 1
            # Down
            if move[0] == 'D':
                head[0] -= 1

            # Adjust tail
            if abs(head[0] - tail[0]) > 1:
                if move[0] == 'U':
                    tail[0] += 1
                if move[0] == 'D':
                    tail[0] -= 1
                tail[1] = head[1]
            if abs(head[1] - tail[1]) > 1:
                tail[0] = head[0]
                if move[0] == 'L':
                    tail[1] -= 1
                if move[0] == 'R':
                    tail[1] += 1

            # Store tail position in visited
            visited.add((tail[0], tail[1]))

    solution_1 = len(visited)
    return solution_1, 0

def parse_input(input):
    input = [x.split(' ') for x in input.splitlines()]
    data = [[x, int(y)] for x, y in input]
    return data

def main():
    test_data = parse_input(example)
    solution_1, solution_2 = solution(test_data)
    assert(solution_1 == 13)
    assert(solution_2 == 0)

    program_file_name = sys.argv[0]
    input_file_name = 'input_' + os.path.splitext(program_file_name)[0] + '.txt'
    data = parse_input(get_input(input_file_name))
    solution_1, solution_2 = solution(data)
    print('Part 1: ', solution_1)
    print('Part 2: ', solution_2)
    
if __name__ == '__main__':
    sys.exit(main())