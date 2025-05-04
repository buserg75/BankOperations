import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('number, expected', [
    ('7000792289606361', '7000 79** **** 6361'),
    ('70007922896063614562', 'Вы ввели некорректный номер карты'),
    ('700079', 'Вы ввели некорректный номер карты'),
    ('ыввыыывы45555ыыввы', 'Вы ввели некорректный номер карты'),
    ('', 'Вы не ввели номер карты')])
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


@pytest.mark.parametrize('number, expected', [
    ('73654108430135874305', '**4305'),
    ('70007922896', 'Вы ввели некорректный номер карты'),
    ('70007925544544545454552896', 'Вы ввели некорректный номер карты'),
    ('ыввыыывы45555ыыввы45', 'Вы ввели некорректный номер карты'),
    ('', 'Вы не ввели номер счета')])
def test_get_mask_account(number, expected):
    assert get_mask_account(number) == expected
