#!/usr/bin/env python3

import sys

file_contents = open(sys.argv[1]).read().strip()

if len(sys.argv) != 3:
    part = 1
else:
    part = int(sys.argv[2])
    
count = 0

digits_as_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in file_contents.split('\n'):
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(c)
        if part == 2:
            for d, val in enumerate(digits_as_strings):
                if line[i:].startswith(val):
                    digits.append(str(d+1))
    score = int(digits[0] + digits[-1])
    count += score

print(count)
