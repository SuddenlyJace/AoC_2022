import sys
import os
from common import get_input

import string

example = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

def solution(data):
    PRIORITY = dict(zip(string.ascii_lowercase + string.ascii_uppercase, list(range(1,53))))
    unique_item_sum = 0
    unique_badge_sum = 0
    group_count = 0
    badges = []

    for rucksack in data:
        compartment_size = int(len(rucksack)/2)
        first_compartment = set(rucksack[:compartment_size])
        second_compartment = set(rucksack[compartment_size:])
        unique_items = first_compartment & second_compartment
        unique_item = next(iter(unique_items))
        unique_item_sum += PRIORITY[unique_item]
        badges.append(set(rucksack))
        group_count += 1

        if group_count == 3:
            badge = (badges[0] & badges[1] & badges[2])
            unique_badge_sum += PRIORITY[next(iter(badge))]
            badges = []
            group_count = 0

    
    return unique_item_sum, unique_badge_sum

def parse_input(input):
    return input.splitlines()

def main():
    test_data = parse_input(example)
    solution_1, solution_2 = solution(test_data)
    assert(solution_1 == 157)
    assert(solution_2 == 70)

    program_file_name = sys.argv[0]
    input_file_name = 'input_' + os.path.splitext(program_file_name)[0] + '.txt'
    data = parse_input(get_input(input_file_name))
    solution_1, solution_2 = solution(data)
    print('Part 1: ', solution_1)
    print('Part 2: ', solution_2)
    
if __name__ == '__main__':
    sys.exit(main())