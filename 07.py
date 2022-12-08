import sys
import os
from common import get_input

example = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''

def solution(data):
    path = []
    dirs = {'/': 0}
    TOTAL_SPACE = 70000000
    UPDATE_SIZE = 30000000

    for line in data:
        params = line.split()
        # Commands
        if params[0] == '$':
            if params [1] == 'cd':
                if params[2] == '..':
                    path.pop()
                elif params[2] == '/':
                    path = []
                else:
                    path.append(params[2])
            if params [1] == 'ls':
                pass
        # Directory Entry
        elif params[0] == 'dir':
            dir = []
            dir.append(params[1])
            directory = '/' + '/'.join(path + dir)
            if (directory) not in dirs:
                dirs[directory] = 0
        # Files
        else:
            # Always add size to root
            dirs['/'] += int(params[0])

            tmp = path.copy()
            for _ in range(len(path)):
                directory = '/' + '/'.join(tmp)
                dirs[directory] += int(params[0])
                tmp.pop()

    answer1 = 0
    for size in list(dirs.values()):
        if size < 100000:
            answer1 += size
    
    dir_sizes = list(dirs.values())
    dir_sizes.sort()
    free_space = TOTAL_SPACE - dirs['/']
    for size in dir_sizes:
        if (free_space + size) >= UPDATE_SIZE:
            answer2 = size
            break

    return answer1, answer2

def parse_input(input):
    return input.splitlines()

def main():
    test_data = parse_input(example)
    solution_1, solution_2 = solution(test_data)
    assert(solution_1 == 95437)
    assert(solution_2 == 24933642)

    program_file_name = sys.argv[0]
    input_file_name = 'input_' + os.path.splitext(program_file_name)[0] + '.txt'
    data = parse_input(get_input(input_file_name))
    solution_1, solution_2 = solution(data)
    print('Part 1: ', solution_1)
    print('Part 2: ', solution_2)
    
if __name__ == '__main__':
    sys.exit(main())