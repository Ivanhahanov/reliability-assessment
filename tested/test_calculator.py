#!/usr/bin/python3
import subprocess
import sys

runs = 0
errors = 0

for line in sys.stdin.readlines():
    result = subprocess.run(f'echo "{line.strip()}" | tested/calculator.py', shell=True, stdout=subprocess.PIPE)
    runs += 1
    if result.returncode != 0:
        errors += 1


print(runs, errors, errors/runs)
