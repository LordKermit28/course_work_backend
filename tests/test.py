import pytest
from utils import output_operations

def test_output_operations():
    operations = [
        {
            "date": "2022-01-01T10:00:00.000000",
            "description": "Пополнение карты",
            "from": "",
            "to": "1234 5678 9012 3456",
            "operationAmount": {"amount": "1000.00", "currency": "RUB"},
            "state": "EXECUTED"
        },
        {
            "date": "2022-01-02T12:00:00.000000",
            "description": "Оплата услуг",
            "from": "0987 6543 2109 8765",
            "to": "",
            "operationAmount": {"amount": "500.00", "currency": "RUB"},
            "state": "EXECUTED"
        },
        {
            "date": "2022-01-03T14:00:00.000000",
            "description": "Перевод на счет другого пользователя",
            "from": "1234 5678 9012 3456",
            "to": "2345 6789 0123 4567",
            "operationAmount": {"amount": "2000.00", "currency": "RUB"},
            "state": "EXECUTED"
        }
    ]
    n = 2

    result = output_operations(operations, n)

    assert result == '''03.01.2022 Перевод на счет другого пользователя
**** 3456 -> **45 4567
2000.00 RUB

02.01.2022 Оплата услуг
98** **** **** 8765 -> 
500.00 RUB

'''