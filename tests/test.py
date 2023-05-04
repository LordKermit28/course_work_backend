import pytest
from utils import output_operations, sorted_operations, make_str_into_digit, mask_card_number, mask_account


@pytest.mark.parametrize('input_data, expected_result', [([{
            "date": "2023-01-02T12:22:10.000001",
            "description": "Перевод на счет другого пользователя",
            "from": "4987 6543 2109 8765",
            "to": "2345 6789 0123 4567",
            "operationAmount": {"amount": "500.00", "currency": {"name": "руб", "code": "RUB"}},
            "state": "EXECUTED"
        }],
          [['02.01.2023',
            'Перевод на счет другого пользователя',
            '498765** **** 8765',
            '**4567',
            '500.00',
            {'code': 'RUB', 'name': 'руб'}]])])


def test_output_operations(input_data, expected_result):

    n = 1

    result = output_operations(input_data, n)

    assert result == expected_result


def test_sort_operation():
    operations = [{'date': '2022-01-05T12:22:10.000001',
                   "description": "Перевод на счет другого пользователя",
                   "from": "4987 6543 2109 8765",
                   "to": "2345 6789 0123 4567",
                   "operationAmount": {"amount": "500.00", "currency": {"name": "руб", "code": "RUB"}},
                   'state': 'EXECUTED'},
                  {'date': '2025-01-05T12:22:10.000001', "description": "Перевод на счет другого пользователя",
                   "from": "4987 6543 2109 8765",
                   "to": "2345 6789 0123 4567",
                   "operationAmount": {"amount": "500.00", "currency": {"name": "руб", "code": "RUB"}},
                   'state': 'EXECUTED'},
                  {'date': '2022-01-02T12:22:10.000001',
                   "description": "Перевод на счет другого пользователя",
                   "from": "4987 6543 2109 8765",
                   "to": "2345 6789 0123 4567",
                   "operationAmount": {"amount": "500.00", "currency": {"name": "руб", "code": "RUB"}},
                   'state': 'CANCELED'}]

    expected_result = [['05.01.2025',
                        'Перевод на счет другого пользователя',
                        '498765** **** 8765',
                        '**4567',
                        '500.00',
                        {'code': 'RUB', 'name': 'руб'}],
                       ['05.01.2022',
                        'Перевод на счет другого пользователя',
                        '498765** **** 8765',
                        '**4567',
                        '500.00',
                        {'code': 'RUB', 'name': 'руб'}]]

    results = output_operations(operations, 3)
    assert results == expected_result


def test_sort_with_wrong_date_format():
    with pytest.raises(ValueError):
        sorted_operations([{"state": "EXECUTED", "date": "2021-10-20 12:30:45"}])
        pytest.xfail("Неверный формат даты")



def test_make_str_into_digit():
    parameters = [('123141', '123141'),
                  ('dlsgmf123', '123'),
                  ('sadfa', ''),
                  ]
    for input, output in parameters:
        assert make_str_into_digit(input) == output

def test_make_test_into_digit_with_bool():
    with pytest.raises(TypeError):
        make_str_into_digit(True)
        pytest.xfail('Неверный формат данных')



@pytest.mark.parametrize('input_number, masked_card_number', [
    ('41241897418', '412418** **** 7418'),
    ('234g2ngf', '2342** **** 2342'),
])
def test_mask_card_number(input_number, masked_card_number):
    assert mask_card_number(input_number) == masked_card_number

@pytest.mark.parametrize('input_number, masked_account_number', [
    ('41241897418', '**7418'),
    ('234g2ngf', '**2342'),
])
def test_mask_account_number(input_number, masked_account_number):
    assert mask_account(input_number) == masked_account_number


    





