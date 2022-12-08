import sys
import os
from common import get_input

example = '''mjqjpqmgbljsphdztnvjfqwrcgsmlb
'''
example2 = '''bvwbjplbgvbhsrlpgdmjqwftvncz
'''
example3 = '''nppdvjthqldpwncqszvftbrmjlhg
'''
example4 = '''nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
'''
example5 = '''zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
'''

def solution(data):
    for i in range(len(data)-3):
        unique = set(data[i:i+4])
        if len(unique) == 4:
            characters_4 = i+4
            break
    
    for i in range(len(data)-13):
        unique = set(data[i:i+14])
        if len(unique) == 14:
            characters_14 = i+14
            break
    
    return characters_4, characters_14

def parse_input(input):
    return input.strip('\n')

def main():
    test_data = parse_input(example)
    test_data2 = parse_input(example2)
    test_data3 = parse_input(example3)
    test_data4 = parse_input(example4)
    test_data5 = parse_input(example5)
    solution_1, solution_2 = solution(test_data)
    assert(solution_1 == 7)
    assert(solution_2 == 19)
    solution_1, solution_2 = solution(test_data2)
    assert(solution_1 == 5)
    assert(solution_2 == 23)
    solution_1, solution_2 = solution(test_data3)
    assert(solution_1 == 6)
    assert(solution_2 == 23)
    solution_1, solution_2 = solution(test_data4)
    assert(solution_1 == 10)
    assert(solution_2 == 29)
    solution_1, solution_2 = solution(test_data5)
    assert(solution_1 == 11)
    assert(solution_2 == 26)

    program_file_name = sys.argv[0]
    input_file_name = 'input_' + os.path.splitext(program_file_name)[0] + '.txt'
    data = parse_input(get_input(input_file_name))
    solution_1, solution_2 = solution(data)
    print('Part 1: ', solution_1)
    print('Part 2: ', solution_2)
    
if __name__ == '__main__':
    sys.exit(main())