# Обработка арифметических операци
# Arithmetic processing


ErrorOperation = 'Unknown operation!\n'


def arithmetic_operation(a, b, operation):
    result = None
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        if b == 0:
            print(ArithmeticError)
        else:
            result = a / b
    else:
        print(ErrorOperation)
    if result is not None:
        return print('The result of an arithmetic operation %s is equal to %0.1f' %
                     (operation, result))  # Результат арифметической операции равен
