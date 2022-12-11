import sys
import os
from common import get_input

import math

example = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
'''

def solution(monkeys, rounds):
    for round in range(rounds):
        print("\n\n---Round "+str(round+1)+"---")
        for m in range(len(monkeys)):
            for item in monkeys[m]['items']:
                if monkeys[m]['operation'][1] == 'old':
                    worry = item
                else:
                    worry = int(monkeys[m]['operation'][1])

                if monkeys[m]['operation'][0] == '+':
                    item += worry
                if monkeys[m]['operation'][0] == '*':
                    item = item * worry

                # Inspected item
                monkeys[m]['num_inspected'] += 1
                item = math.floor(item/3)

                # Throw items
                if item % monkeys[m]['test']['test'] == 0:
                    monkeys[monkeys[m]['test']['true']]['items'].append(item)
                else:
                    monkeys[monkeys[m]['test']['false']]['items'].append(item)

            # This Monkey threw all their items
            monkeys[m]['items'] = []

        for monkey in monkeys:
            print(monkey)
    
    monkey_buisness = [monkey['num_inspected'] for monkey in monkeys]
    monkey_buisness.sort(reverse=True)

    return monkey_buisness[0] * monkey_buisness[1]

def parse_input(input):
    monkey_input = input.split('\n\n')
    monkeys = []
    
    for monkey_attributes in monkey_input:
        attributes = monkey_attributes.splitlines()
        monkey = {}
        
        # Monkey #
        i = int(attributes[0].split()[1].strip(':'))

        # Starting items
        if attributes[1].split(":")[0] != '  Starting items':
            raise Exception("Starting items must be the 2nd line")
        
        items = attributes[1].split(":")[1].split(',')
        items = [int(i.strip(' ')) for i in items]
        
        if len(monkeys) != i:
            e = "Expected Monkey "+ str(i) +", got Monkey "+ str(len(monkeys))
            raise Exception(e)
        monkey['items'] = items

        # Operation
        if attributes[2].split(":")[0] != '  Operation':
            raise Exception("Operation must be the 3nd line")
        operation = attributes[2].split(":")[1].split('new = old')[1].strip(' ').split()
        
        if len(monkeys) != i:
            e = "Expected Monkey "+ str(i) +", got Monkey "+ str(len(monkeys))
            raise Exception(e)
        monkey['operation'] = operation  

        # Test and throw
        if attributes[3].split(":")[0] != '  Test':
            raise Exception("Test must be the 4th line")
        if attributes[3].split(":")[1].split('by')[0].strip() != 'divisible':
            raise Exception("Test must be for divisibility")
        test = {'test': int(attributes[3].split(":")[1].split('by')[1].strip(' '))}
        
        if attributes[4].split(":")[0] != '    If true':
            raise Exception("Test for true must be the 5th line")
        test['true'] = int(attributes[4].split('monkey')[-1])
        
        if attributes[5].split(":")[0] != '    If false':
            raise Exception("Test for false must be the 6th line")
        test['false'] = int(attributes[5].split('monkey')[-1])
        
        if len(monkeys) != i:
            e = "Expected Monkey "+ str(i) +", got Monkey "+ str(len(monkeys))
            raise Exception(e)
        monkey['test'] = test   

        # Build Monkeys
        monkey['num_inspected'] = 0
        monkeys.append(monkey)

    return monkeys

def main():
    test_data = parse_input(example)
    solution_1 = solution(test_data, 20)
    assert(solution_1 == 10605)

    program_file_name = sys.argv[0]
    input_file_name = 'input_' + os.path.splitext(program_file_name)[0] + '.txt'
    data = parse_input(get_input(input_file_name))
    solution_1 = solution(data, 20)
    print('Part 1: ', solution_1)
    
if __name__ == '__main__':
    sys.exit(main())