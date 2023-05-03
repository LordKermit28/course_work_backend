import pytest
from utils import output_operations

def test_output_operations():
    operations = {
            "date": "2023-01-02T12:22:10.000001",
            "description": "Перевод на счет другого пользователя",
            "from": "4987 6543 2109 8765",
            "to": "2345 6789 0123 4567",
            "operationAmount": {"amount": "500.00", "currency": {"name": "руб", "code": "RUB"}},
            "state": "EXECUTED"
        },
        # {
        #     "date": "2023-01-03T14:00:00.000000",
        #     "description": "Перевод на счет другого пользователя",
        #     "from": "1234 5678 9012 3456",
        #     "to": "2345 6789 0123 4567",
        #     "operationAmount": {"amount": "2000.00", "currency": {"name": "руб.", "code": "RUB"}},
        #     "state": "CANCELED"
        # },
    # {
    #     "date": "2023-01-01T10:00:00.000000",
    #     "description": "Пополнение карты",
    #     "from": "",
    #     "to": "1234 5678 9012 3456",
    #     "operationAmount": {"amount": "1000.00", "currency": {"name": "руб.", "code": "RUB"}},
    #     "state": "EXECUTED"
    # },

    n = 1

    result = output_operations(operations, n)

    assert result == [['02.01.2023', "Перевод на счет другого пользователя", ' 498765** **** 8765', '**4567', '500.00', {'name': 'руб', 'code': 'RUB'}]]