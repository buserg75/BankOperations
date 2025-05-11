from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> List[Dict[str, Any]]:
    """Функция, которая принимает на вход список словарей. Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)"""
    return (i for i in transactions if i.get("operationAmount", []).get("currency", []).get("code", []) == currency)


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[dict[str, Any]]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction.get('description', 'Нет описания')


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генератор принимает значения start и stop в качестве аргумента и который выдает номера банковских карт
    в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты"""
    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        formatted_card_number = " ".join([card_number[i:i + 4] for i in range(0, 16, 4)])
        if start == stop:
            yield 'Start не может быть равен Stop'
        else:
            yield formatted_card_number


for card_number in card_number_generator(1, 5):
    print(card_number)
