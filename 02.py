import sys
import os
from common import get_input

example = '''A Y
B X
C Z'''

STRATEGY_TRANSLATOR = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors'
}

VICTORY_TRANSLATOR = {
    'X': 'Lose',
    'Y': 'Draw',
    'Z': 'Win'
}

SCORE = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3,
    'Lose': 0,
    'Draw': 3,
    'Win': 6
}

# Opponent is on the left, Player on right
RESULTS = {
    'Rock': {'Rock': 'Draw', 'Paper': 'Win', 'Scissors': 'Lose'},
    'Paper': {'Rock': 'Lose', 'Paper': 'Draw', 'Scissors': 'Win'},
    'Scissors': {'Rock': 'Win', 'Paper': 'Lose', 'Scissors': 'Draw'}
}

def round_result(opponent, player):
    score = SCORE[player]
    score += SCORE[RESULTS[opponent][player]]
    
    return score

def solution(data):
    score = 0

    for match in data:
        opponent_encoded, player_encoded = match
        opponent = STRATEGY_TRANSLATOR[opponent_encoded]
        player = STRATEGY_TRANSLATOR[player_encoded]

        score += round_result(opponent, player)

    return score


def solution2(data):
    score = 0

    # Reverse mapping
    for match in data:
        opponent_encoded, result_encoded = match
        result = VICTORY_TRANSLATOR[result_encoded]
        opponent = STRATEGY_TRANSLATOR[opponent_encoded]
        player = dict((v, k) for k, v in RESULTS[opponent].items())[result]

        score += round_result(opponent, player)

    return score

def parse_input(input):
    matrix = input.splitlines()
    # Make matrix from input
    return([[cell for cell in row.replace(' ','')] for row in matrix])

def main():
    test_data = parse_input(example)
    assert(solution(test_data) == 15)
    assert(solution2(test_data) == 12)

    program_file_name = sys.argv[0]
    input_file_name = 'input_' + os.path.splitext(program_file_name)[0] + '.txt'
    data = parse_input(get_input(input_file_name))
    print('Part 1: ', solution(data))
    print('Part 2: ', solution2(data))
    
if __name__ == '__main__':
    sys.exit(main())