#!/usr/bin/env python3

import sys

class Game:
    def __init__(self, game_index: int, max_colors: dict):
        self.game_index = game_index
        self.max_colors = max_colors
    
    def __str__(self) -> str:
        return f'Game: {self.game_index}, Colors: {self.max_colors}'
    
    def is_possible(self, num_red, num_green, num_blue) -> bool:
        if self.max_colors['red'] <= num_red and self.max_colors['green'] <= num_green and self.max_colors['blue'] <= num_blue:
            return True
        return False
    
    def get_power(self) -> int:
        answer = 1
        for value in self.max_colors.values():
            answer *= int(value)
        return answer

def line_parser(line: str) -> Game:
    max_colors = {}
    split_line = line.split(':', 1)
    game_index = split_line[0].split(' ')[1]
    handfuls = split_line[1].strip().split(';')
    for handful in handfuls:
        num_each_cubes_in_handful = handful.split(',')
        for num_each_cube in num_each_cubes_in_handful:
            num_each_cube = num_each_cube.strip()
            num, color = num_each_cube.split()
            max_colors[color] = max(max_colors.setdefault(color, 0), int(num))
    return Game(game_index, max_colors)


file_contents = open(sys.argv[1]).read().strip()

games = []
for line in file_contents.split('\n'):
    games.append(line_parser(line))

num_red = 12
num_green = 13
num_blue = 14
count = 0
power = 0
for game in games:
    if game.is_possible(num_red, num_green, num_blue):
        count += int(game.game_index)
    power += game.get_power()

print(f'Count: {count}')
print(f'Power: {power}')

