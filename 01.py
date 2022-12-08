import sys
import os
from common import get_input

example = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''

def top_three_elves(elves):
    elves.sort(reverse = True)
    return (sum(elves[0:3]))

def parse_elves(data):
    # Combine calories into elves
    elves = []
    total_calories = 0

    for calories in data:
        if calories != '':
            total_calories += int(calories)
        else:
            elves.append(total_calories)
            total_calories = 0

    # Get last elf
    elves.append(total_calories)
    
    return(elves)

def parse_input(input):
    return(input.splitlines())

def main():
    test_data = parse_input(example)
    elves = parse_elves(test_data)
    assert(max(elves) == 24000)
    assert(top_three_elves(elves) == 45000)

    program_file_name = sys.argv[0]
    input_file_name = 'input_' + os.path.splitext(program_file_name)[0] + '.txt'
    data = parse_input(get_input(input_file_name))
    elves = parse_elves(data)
    print('Part 1: ', max(elves))
    print('Part 2: ', top_three_elves(elves))
    
if __name__ == '__main__':
    sys.exit(main())