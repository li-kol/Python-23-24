import typing as tp
import math

two_operands = ['+', '-', '*', '**', '/']
one_operand = ['ln', '^2', 'sin', 'cos', 'tan', 'lg']
# type: ignore
def calc_two(num_1: float, num_2: float, command: str) -> tp.Union[float, str]:
    if command == "+":
        result = num_1 + num_2
        return result
    if command == "-":
        return num_1 - num_2
    if command == "*":
        return num_1 * num_2
    if command == "/":
        while num_2==0:
               num_2 = float(input("Деление на ноль. Введите ненулевое второе число > "))
        return num_1 / num_2
    if command == "**":
        return num_1 ** num_2


def calc_one(num_1: float, command: str) -> tp.Union[float, str]:
    # type: ignore
    if command == "ln":
        while num_1<=0:
            num_1 = float(input("Аргумент логарифма меньше или равен нулю. Введите аргумент больше нуля > "))
        return math.log(num_1)
    if command == "lg":
        while num_1<=0:
            num_1 = float(input("Аргумент логарифма меньше или равен нулю. Введите аргумент больше нуля > "))
        return math.log(num_1, 10)
    if command == "^2":
        return num_1 ** 2
    if command == "sin":
        return math.sin(num_1)
    if command == "cos":
        return math.cos(num_1)
    if command == "tan":
        return math.tan(num_1)


if __name__ == "__main__":
    while True:  # программа выполняется до ввода 0 вместо команды
        command = input("Введите операцию > ")
        if command.isdigit() and int(command) == 0:
            break
        if command in two_operands:
            while True:
                try:
                    num_1 = float(input("Первое число > "))
                    break  # Break out of the num_1 input loop if no ValueError is raised
                except ValueError:
                    print("Ошибка: Введите число без символов и букв")

            while True:  # Start a new loop for num_2 input
                try:
                    num_2 = float(input("Второе число > "))
                    break
                except ValueError:
                    print("Ошибка: Введите число без символов и букв")
                except ZeroDivisionError:
                    print("Ошибка. Деление на ноль")
            result = calc_two(num_1, num_2, command)
            print(result)  # Break out of the num_2 input loop if no ValueError is raised

        elif command in one_operand:
            try:
                num_1 = float(input("Первое число > "))
            except ValueError:
                print("Ошибка: Введите числа без символов и букв")
            result = calc_one(num_1, command)
            print(result)
        else:
            print(f"Неизвестный оператор: {command!r}.")
            print("Принимаемые операторы:", (two_operands + one_operand))

# while result <= NUM_1 ** 2:
# result = calc(NUM_1+1, NUM_2+1, command)
# print(result)
#  PUT YOUR CODE HERE
