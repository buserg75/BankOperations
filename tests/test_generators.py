import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions, currency, filtered_transactions_1):
    assert list(filter_by_currency(transactions, currency)) == filtered_transactions_1


def test_filter_by_currency_2(transactions, currency_2, filtered_transactions_2):
    assert list(filter_by_currency(transactions, currency_2)) == filtered_transactions_2


def test_filter_by_currency_3(transactions, currency_3, non_transactions):
    assert list(filter_by_currency(transactions, currency_3)) == non_transactions


def test_filter_by_currency_with_empty_list():
    empty_transactions = []
    currency = "USD"
    assert list(filter_by_currency(empty_transactions, currency)) == []


def test_transaction_descriptions(transactions):
    generator = transaction_descriptions(transactions)
    assert next(generator) == 'Перевод организации'
    assert next(generator) == 'Перевод со счета на счет'
    assert next(generator) == 'Перевод со счета на счет'
    assert next(generator) == 'Перевод с карты на карту'
    assert next(generator) == 'Перевод организации'


def test_transaction_descriptions_with_empty_list():
    empty_list = []
    assert list(transaction_descriptions(empty_list)) == []


@pytest.mark.parametrize('start, stop, expected', [
        (0, 1, '0000 0000 0000 0000'),
        (1, 5, '0000 0000 0000 0001'),
        (1, 1, 'Start не может быть равен Stop'),
        (10, 12, '0000 0000 0000 0010')])
def test_card_number_generator(start, stop, expected):
    gen = card_number_generator(start, stop)
    assert next(gen) == expected
