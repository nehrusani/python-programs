import sys

if len(sys.argv) != 4:
    print("Usage: python test.py num1 operator num2")
else:
    a = int(sys.argv[1])
    op = sys.argv[2]   # operator as string
    b = int(sys.argv[3])

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b
    else:
        print("Unsupported operator:", op)
        sys.exit(1)

    print(f"Result: {a} {op} {b} = {result}")