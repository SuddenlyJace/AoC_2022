import sys
import os
from common import get_input

example = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

def solution(data):
    fully_contained = 0
    overlap = 0
    
    for pairs in data:
        low, high = pairs[0].split('-')
        section_1 = set(list(range(int(low), int(high)+1)))
        low, high = pairs[1].split('-')
        section_2 = set(list(range(int(low), int(high)+1)))
        combined_section = section_1 & section_2

        if combined_section == section_1 or combined_section == section_2:
            fully_contained += 1
        if combined_section != set():
            overlap += 1

    return fully_contained, overlap

def parse_input(input):
    pairs = input.splitlines()
    return [pair.split(',') for pair in pairs]

def main():
    test_data = parse_input(example)
    solution_1, solution_2 = solution(test_data)
    assert(solution_1 == 2)
    assert(solution_2 == 4)

    program_file_name = sys.argv[0]
    input_file_name = 'input_' + os.path.splitext(program_file_name)[0] + '.txt'
    data = parse_input(get_input(input_file_name))
    solution_1, solution_2 = solution(data)
    print('Part 1: ', solution_1)
    print('Part 2: ', solution_2)
    
if __name__ == '__main__':
    sys.exit(main())