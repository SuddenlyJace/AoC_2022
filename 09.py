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

def solution(data, rope_size):
    rope = [[0, 0] for x in range(rope_size)]
    visited = set()
    
    for move in data:
        # Number of moves
        for _ in range(move[1]):
            # Up
            if move[0] == 'U':
                rope[0][0] += 1
            # Left
            if move[0] == 'L':
                rope[0][1] -= 1
            # Right
            if move[0] == 'R':
                rope[0][1] += 1
            # Down
            if move[0] == 'D':
                rope[0][0] -= 1

            # Adjust knots
            for i in range(1, rope_size):
                if abs(rope[i-1][0] - rope[i][0]) > 1:
                    if move[0] == 'U':
                        rope[i][0] += 1
                    if move[0] == 'D':
                        rope[i][0] -= 1
                    rope[i][1] = rope[i-1][1]
                if abs(rope[i-1][1] - rope[i][1]) > 1:
                    rope[i][0] = rope[i-1][0]
                    if move[0] == 'L':
                        rope[i][1] -= 1
                    if move[0] == 'R':
                        rope[i][1] += 1

            # Store tail position in visited
            visited.add((rope[rope_size-1][0], rope[rope_size-1][1]))

    return len(visited)

def parse_input(input):
    input = [x.split(' ') for x in input.splitlines()]
    data = [[x, int(y)] for x, y in input]
    return data

def main():
    test_data = parse_input(example)
    solution_1 = solution(test_data, 2)
    solution_2 = solution(test_data, 10)
    assert(solution_1 == 13)
    assert(solution_2 == 1)

    program_file_name = sys.argv[0]
    input_file_name = 'input_' + os.path.splitext(program_file_name)[0] + '.txt'
    data = parse_input(get_input(input_file_name))
    solution_1 = solution(data, 2)
    assert(solution_1 == 6057)
    solution_2 = solution(data, 10)
    print('Part 1: ', solution_1)
    print('Part 2: ', solution_2)
    
if __name__ == '__main__':
    sys.exit(main())