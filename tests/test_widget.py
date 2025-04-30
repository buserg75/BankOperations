import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize('type_numbers, expected', [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
    ('', 'Вы не ввели номер карты или счета'),
    ('Maestro 15968378687051999998', 'Вы ввели некорректные данные'),
    ('Счет 6468647367', 'Вы ввели некорректные данные')
    ])

def test_mask_account_card(type_numbers, expected):
    assert mask_account_card(type_numbers) == expected


@pytest.mark.parametrize('date_string, expected', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2025-04-30T02:26:18.671407', '30.04.2025'),
    ('2023-04-SS30T02:26:18.671407', 'Вы ввели некорректную дату'),
    ('', 'Вы ввели некорректную дату')
    ])

def test_get_date(date_string, expected):
    assert get_date(date_string) == expected

