string = input("Введите строку текста: ")
width = int(input("Введите количество символов для отформатированной строки: " ))
symbol = input("Введите символ для заполнения дополнения в отформатированной строки: ")

def corrector(string, width, symbol):
    count = width - len(string)
    half = count/2
    result = ''
    result_plus = ''

    if (half.is_integer()):
        pass
    else:
        result_plus = symbol

    i = 1
    while(i <= half):
        result = result + symbol
        i = i + 1

    result = result + result_plus + string + result

    return result


print (corrector(string, width, symbol))
