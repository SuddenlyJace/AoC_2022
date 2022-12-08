import sys
import os
from common import get_input

from copy import deepcopy

example = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

def solution(stacks, moves):
    stacks_part2 = deepcopy(stacks)

    
    # Part 1
    for move in moves:
        for _ in range(move[0]):
            stacks[move[2]].append(stacks[move[1]].pop())
    
    result = ''
    for stack in stacks:
        result += stack.pop()

    # Part 2
    for move in moves:
        crates_in_motion = stacks_part2[move[1]][-move[0]:]
        stacks_part2[move[1]] = stacks_part2[move[1]][:-move[0]]
        stacks_part2[move[2]] = stacks_part2[move[2]] + crates_in_motion
    
    result_part2 = ''
    for stack in stacks_part2:
        result_part2 += stack.pop()

    return result, result_part2

def parse_input(input):
    input_drawing, input_procedure = input.split('\n\n')
    
    rows = input_drawing.splitlines()
    num_stacks = int((len(rows.pop())+1)/4)
    stacks = [ [] for _ in range(num_stacks)]
    
    for row in reversed(rows):
        for offset in range(num_stacks):
            crate = row[(offset*4) + 1]
            if crate != ' ':
                stacks[offset].append(crate)

    procedure = input_procedure.splitlines()
    moves = []
    for move in procedure:
        moves.append([int(s) for s in move.split() if s.isdigit()])
    
    # Adjust index
    moves = [(one, two - 1, three - 1) for (one, two, three) in moves]

    return stacks, moves

def main():
    test_stacks, test_moves = parse_input(example)
    solution_1, solution_2 = solution(test_stacks, test_moves)
    assert(solution_1 == 'CMZ')
    assert(solution_2 == 'MCD')

    program_file_name = sys.argv[0]
    input_file_name = 'input_' + os.path.splitext(program_file_name)[0] + '.txt'
    stacks, moves = parse_input(get_input(input_file_name))
    solution_1, solution_2 = solution(stacks, moves)
    print('Part 1: ', solution_1)
    print('Part 2: ', solution_2)
    
if __name__ == '__main__':
    sys.exit(main())