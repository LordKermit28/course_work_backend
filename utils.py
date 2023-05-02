import json
from datetime import datetime

def get_data(file_path):
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)
        return data

def make_str_into_digit(line: str):
    digit_str = ""
    for s in line:
        if s.isdigit():
            digit_str += s
    return digit_str

    # Функция для маскирования номера карты
def mask_card_number(card_number):
    card_number = make_str_into_digit(card_number)
    return f"{card_number[:6]} {'*'*4} {'*'*4} {card_number[-4:]}"

    # Функция для маскирования номера счета
def mask_account(account_number):
    account_number = make_str_into_digit(account_number)
    return f"**{account_number[-4:]}"

# Сортируем операции по дате (в обратном порядке)
def sorted_operations(operations):
    return sorted([op for op in operations if op.get('state') == 'EXECUTED'], key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)

def output_operations(operations):

    operations = sorted_operations(operations)

    for operation in operations[:5]:
        date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        operation_type = operation['description']
        amount, currency = operation['operationAmount'].values()
        from_account = operation.get('from')
        to_account = operation['to']

        if not from_account or not to_account:
            from_account = ""
            to_account = ""

        from_account = mask_card_number(from_account)
        to_account = mask_account(to_account)

        # Выводим информацию об операции
        print(f"{date} {operation_type}")
        print(f"{from_account} -> {to_account}")
        print(f"{amount} {currency}")
        print()

data = get_data("operations.json")

output_operations(data)