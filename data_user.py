# Данные введеные пользователем
# User data entered

ErrorInput = 'Input integer!\n'

while True:
    try:
        number_1 = float(input('Enter firs number:\n'))
        number_2 = float(input('Enter second number:\n'))
        if type(number_1 and number_2) == float:
            break
    except:
        print(ErrorInput)

operation = input('Enter operation:\n')
