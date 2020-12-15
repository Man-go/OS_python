#!/usr/bin/env python3


def eval_expr(s, d={}):
    stack = []
    binoper = ["+", "-", "*", "/"]
    str_element = s.split()

    if len(d) != 0:
        for i, n in enumerate(str_element):
            if n in d:
                str_element[i] = d[n]

    for n in str_element:
        if n not in binoper:
            stack.append(int(n))
        else:
            if n == "+":
                stack.append(stack.pop(-2) + stack.pop(-1))
            elif n == "-":
                stack.append(stack.pop(-2) - stack.pop(-1))
            elif n == "*":
                stack.append(stack.pop(-2) * stack.pop(-1))
            else:
                stack.append(stack.pop(-2) // stack.pop(-1))
    return stack.pop()


def to_infix(s):
    stack = []
    binoper = ["+", "-", "*", "/"]
    str_element = s.split()

    for n in str_element:
        if n not in binoper:
            stack.append(n)
        else:
            print("else")
            stack.append(f'( {stack.pop(-2)} {n} {stack.pop(-1)} )')

    return stack.pop()


def to_postfix(s):
    lex = s.strip().split()
    s2 = []
    stack = []
    binoper = ["+", "-", "*", "/", "(", ")"]
    for n in lex:
        if n == "(":
            s2 = [n] + s2
        elif n in binoper:
            if s2 == []:
                s2 = [n]
            elif n == ")":
                while(True):
                    q = s2[0]
                    s2 = s2[1:]
                    if q == "(":
                        break
                    stack += [q]
            elif priority(s2[0]) < priority(n):
                s2 = [n] + s2
            else:
                while(True):
                    if s2 == []:
                        break
                    q = s2[0]
                    stack += [q]
                    s2 = s2[1:]
                    if priority(q) == priority(n):
                        break
                s2 = [n] + s2
        else:
            stack += [n]
    while(s2 != []):
        q = s2[0]
        stack += [q]
        s2 = s2[1:]
    return " ".join(stack)


def priority(pr):
    if pr == "+" or pr == "-":
        return 1
    elif pr == "*" or pr == "/":
        return 2
    elif pr == "(":
        return 0
