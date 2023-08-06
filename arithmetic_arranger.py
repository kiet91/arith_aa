from functools import cache
from re import search, findall


def arithmetic_arranger(problems, tooutput: bool = False):  # tooupt: True -> calculate and print the equation
    if len(problems) > 5:
        return 'Error: Too many problems.'  # comment this to enter more than 5
    up_num: str = ''
    down_num: str = ''
    div: str = ''  # the line
    space = ' '
    ans: str = ''

    @cache  # type list is really inefficient ^^
    def backtozero(number1: int, number2: int):  # set len from list (align num to the right)
        var = number1 - number2
        if var <= 0:
            return [- var, 0]
        return [0, var]

    def addifTrue(numberl, quotation):
        if quotation == '+':
            return str(numberl[0] + numberl[1])
        return str(numberl[0] - numberl[1])

    for arith in problems:
        try:
            y = search(r"[+-]", arith).group()  # find the quotation (+ or -)
        except AttributeError:
            return "Error: Operator must be '+' or '-'."  # will support multiplication later
        x = findall(r"\b[0-9]\w*", arith)  # lists of numbers
        try:
            x1 = list(map(lambda blu: int(blu), x))
        except ValueError:
            return "Error: Numbers must only contain digits."
        x2 = list(map(lambda blu: len(blu), x))
        # if x2[0] >= 5 or x2[1] >= 5:
        #     return "Error: Numbers cannot be more than four digits."
        b = backtozero(x2[0], x2[1])
        up_num += f"  {space * b[0]}{x[0]}    "
        down_num += f"{y} {space * b[1]}{x[1]}    "
        div += f"{'-' * (max(x2) + 2)}    "
        if tooutput:
            r = addifTrue(x1, y)
            setq = 1
            if int(r) < 0:
                setq = 0
            elif len(r) < max(x2):
                setq = max(x2) - len(r) + 1
            elif len(r) > max(x2):
                setq = len(r) - max(x2)
            ans += f" {space * setq}{r}    "
    arranged_problems = f"{up_num.rstrip()}\n{down_num.rstrip()}\n{div.rstrip()}\n{ans.rstrip()}"

    return arranged_problems
