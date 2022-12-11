import sys
import os
from common import get_input

example = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
'''

def solution(data):
    X = 1
    program = []
    CRT = ''

    for instruction in data:
        if instruction[0] == 'noop':
            program.append(0)
        if instruction[0] == 'addx':
            program.append(0)
            program.append(int(instruction[1]))

    signal = []
    for i in range(240):
        # Draw CRT
        if (abs(X - (i%40)) <= 1):
            CRT += '#'
        else:
            CRT += '.'
        # Record value before instruction completes
        if ((i+21) % 40) == 0:
            signal.append(X*(i+1))
        X += program[i%len(program)]

    # Display CRT
    n = 40
    for line in [CRT[i:i+n] for i in range(0, len(CRT), n)]:
        print(line)
    return sum(signal)

def parse_input(input):
    return [x.split(' ') for x in input.splitlines()]

def main():
    test_data = parse_input(example)
    solution_1 = solution(test_data)
    assert(solution_1 == 13140)

    program_file_name = sys.argv[0]
    input_file_name = 'input_' + os.path.splitext(program_file_name)[0] + '.txt'
    data = parse_input(get_input(input_file_name))
    solution_1 = solution(data)
    print('Part 1: ', solution_1)
    
if __name__ == '__main__':
    sys.exit(main())