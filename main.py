from utils import output_operations, get_data, print_output

if __name__ == "__main__":
    date = get_data('operations.json')

    while True:
        user_input = input('Введите стоп, чтобы закончить\nВведите количество выполненных операций, которое вы хотите увидеть: ')
        if user_input == 'стоп' or user_input == 'stop':
            break
        else:
            try:
                n = int(user_input)
                operations = output_operations(date, n)
                print_output(operations)
            except ValueError:
                print('Вы ввели не число и не стоп!')
            except TypeError:
                print('Вы ввели не корректное значение!')
            except:
                print('Произошла непредвиденная ошибка!')




