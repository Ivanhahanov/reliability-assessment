#!/usr/bin/python3
import sys


def parse(data: str):
    arg1 = ""
    action = ""
    arg2 = ""
    for symbol in data:
        if action == "":
            if symbol.isnumeric():
                arg1 += symbol
            elif symbol == " ":
                continue
            elif symbol == ".":
                arg1 += symbol
            else:
                action = symbol
        else:
            arg2 += symbol
    return float(arg1), action, float(arg2)


def calc(action, a, b):
    if action == "+":
        return a + b
    elif action == "-":
        return a - b
    elif action == "*":
        return a * b
    elif action == "/":
        return a / b
    else:
        return f"unknown action {action}"


def main():
    try:
        a, action, b = parse(sys.stdin.readline())
        print(a, action, b, end=" = ")
    except Exception as e:
        print(e)
        return 1

    try:
        result = calc(action, a, b)
        print(result)
    except Exception as e:
        print("error")
        print(e)
        return 1
    return 0


exit(main())
