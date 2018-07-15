def is_arithmetic_symbol(symbol):
    if (symbol.strip() == '+') or (symbol.strip() == '-') or (symbol.strip() == '*') or (symbol.strip() == '%'):
        return True
    else:
        return False


def is_braces(symbol):
    if (symbol.strip() == '(') or (symbol.strip() == '{') or (symbol.strip() == ')') or (symbol.strip() == '}'):
        return True
    else:
        return False


def is_integer(symbol):
    return symbol.strip().isdigit()


def has_higher_priority(param, param1):
    if not is_arithmetic_symbol(param1):
        return True
    else:
        arith_symbols = ['/', '*', '+', '-']
        if arith_symbols.index(param) <= arith_symbols.index(param1):
            return True
        else:
            return False


def to_postfix(string):
    infix_list = string.split()
    infix_list_copy = []

    for i in range(0, len(infix_list)):
        if (infix_list[i].strip() == '(') or (infix_list[i].strip() == '{'):
            if i != 0 and i != (len(infix_list) - 1):
                if not is_arithmetic_symbol(infix_list[i - 1]):
                    infix_list_copy.append('*')
                    infix_list_copy.append(infix_list[i].strip())
                else:
                    infix_list_copy.append(infix_list[i].strip())
        elif (infix_list[i].strip() == ')') or (infix_list[i].strip() == '}'):
            if i != 0 and i != (len(infix_list) - 1):
                if not is_arithmetic_symbol(infix_list[i - 1]):
                    infix_list_copy.append(infix_list[i].strip())
                    infix_list_copy.append('*')
        else:
            infix_list_copy.append(infix_list[i].strip())

    operator_stack = []
    operand_queue = []

    for i in range(0, len(infix_list_copy)):
        if is_integer(infix_list_copy[i]):
            operand_queue.append(infix_list_copy[i])
        elif is_braces(infix_list_copy[i]):
            if infix_list_copy[i].strip() == '(' or infix_list_copy[i] == '{':
                operator_stack.append(infix_list_copy[i])
            else:
                if infix_list_copy[i] == ')':
                    while operator_stack[len(operator_stack) - 1] != '(':
                        operand_queue.append(operator_stack.pop())
                else:
                    while operator_stack[len(operator_stack) - 1] != '{':
                        operand_queue.append(operator_stack.pop())
                operator_stack.pop()
        elif is_arithmetic_symbol(infix_list_copy[i]):
            if len(operator_stack) == 0:
                operator_stack.append(infix_list_copy[i])
            elif has_higher_priority(infix_list_copy[i], operator_stack[len(operator_stack) - 1]):
                operator_stack.append(infix_list_copy[i])
            else:
                operand_queue.append(operator_stack.pop())
                operator_stack.append(infix_list_copy[i])
    while len(operator_stack) != 0:
        str = operator_stack.pop()
        if not is_braces(str):
            operand_queue.append(str)

    return operand_queue


def get_val(symbol, param1, param2):
    param1 = int(param1)
    param2 = int(param2)

    if symbol == '+':
        return param2 + param1
    elif symbol == '-':
        return param2 - param1
    elif symbol == '*':
        return param2 * param1
    elif symbol == '/':
        return param2 / param1


def get_result(postfix_list):
    opearand_stack = []
    for i in range (0, len(postfix_list)):
        if not is_arithmetic_symbol(postfix_list[i]):
            opearand_stack.append(postfix_list[i])
        else:
            symbol = postfix_list[i]
            param1 = opearand_stack.pop()
            param2 = opearand_stack.pop()
            val = get_val(symbol, param1, param2)
            opearand_stack.append(val)

    return opearand_stack.pop()


def evaluate(string):
    postfix_list = to_postfix(string)
    result = get_result(postfix_list)
    return result


def reformat(string):
    string = string.replace("+", " + ")
    string = string.replace("-", " - ")
    string = string.replace("*", " * ")
    string = string.replace("/", " / ")
    string = string.replace("(", " ( ")
    string = string.replace(")", " ) ")
    string = string.replace("{", " { ")
    string = string.replace("}", " } ")
    string = string.replace("  ", " ")
    string = string.strip()
    return string


if __name__ == '__main__':
    str = input()
    str = reformat(str)
    print(evaluate(str))