import json
from datetime import datetime

def get_data(file_name):
    with open(file_name, encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as error:
            print("Erros of reading file", error)
            data = None
        return data

def make_str_into_digit(line: str):
    try:
        digit_str = ""
        for s in line:
            if s.isdigit():
                digit_str += s
        result = digit_str
    except TypeError as e:
        print(e)
        result = None
    return result

def mask_card_number(card_number: str):
    card_number = make_str_into_digit(card_number)
    try:
        result = f"{card_number[:6]}{'*'*2} {'*'*4} {card_number[-4:]}"
    except TypeError as e:
        print(f"Вы должны ввести строковой тип данных\nВы вызвали ошибку {e}")
        result = None
    return result

def mask_account(account_number: str):
    try:
        account_number = make_str_into_digit(account_number)
        result =  f"**{account_number[-4:]}"
    except TypeError as e:
        print(f"Вы должны ввести строковой тип данных\nВы вызвали ошибку {e}")
        result = None
    return result


def sorted_operations(operations):
    return sorted([op for op in operations if op.get('state') == 'EXECUTED'], key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)



def output_operations(operations, n: int):

    operations = sorted_operations(operations)
    output = []
    for operation in operations[:n]:
        try:
            date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        except (ValueError, TypeError):
            date = ''
        operation_type = operation['description']
        amount, currency = operation['operationAmount'].values()
        from_account = operation.get('from')
        to_account = operation['to']
        if not from_account:
            from_account = ""
        if not to_account:
            to_account = ""

        from_account = mask_card_number(from_account)
        to_account = mask_account(to_account)

        output.append([date, operation_type, from_account, to_account, amount, currency])

    return output


def print_output(list: list):
    for element in list:
        print(f"{element[0]} {element[1]}")
        print(f"{element[2]} -> {element[3]}")
        print(f"{element[4]} {element[5]['name']}")
        print()
