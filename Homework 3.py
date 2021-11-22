def arithmetic ( a, b, oper):
    if oper == "*":
        return a * b
    elif oper == "/":
        return a / b
    elif oper == "+":
        return a+b
    elif oper == "-":
        return a-b
    else:
        print("Not known operation")
        return 0