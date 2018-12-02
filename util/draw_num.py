import random

numbers = []

numbers.append(["XXXXX", "X   X", "X   X", "X   X", "XXXXX"])
numbers.append(["  X  ", " XX  ", "  X  ", "  X  ", "XXXXX"])
numbers.append(["XXXXX", "    X", " XXX ", "X    ", "XXXXX"])
numbers.append(["XXXXX", "   XX", " XXX ", "   XX", "XXXXX"])
numbers.append(["X   X", "X   X", "XXXXX", "    X", "    X"])
numbers.append(["XXXXX", "X    ", " XXX ", "    X", "XXXXX"])
numbers.append(["XXXXX", "X    ", "XXXXX", "X   X", "XXXXX"])
numbers.append(["XXXXX", "    X", "    X", "    X", "    X"])
numbers.append(["XXXXX", "X   X", " XXX ", "X   X", "XXXXX"])
numbers.append(["XXXXX", "X   X", "XXXXX", "    X", "XXXXX"])

def print_num(x):
        i = 0

        while i < 5:
                num_string = ""
                y = x
                while y > 0:
                        num_string = numbers[int(y % 10)][i] + "   " + num_string
                        y = int(y / 10)
                i += 1
                print(num_string)
