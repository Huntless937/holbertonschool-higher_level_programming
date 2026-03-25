#!/usr/bin/python3
import sys
import calculator_1

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op == '+':
        res = calculator_1.add(a, b)
    elif op == '-':
        res = calculator_1.sub(a, b)
    elif op == '*':
        res = calculator_1.mul(a, b)
    elif op == '/':
        res = calculator_1.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, op, b, res))
