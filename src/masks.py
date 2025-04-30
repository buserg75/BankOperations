def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает на вход номер карты в виде числа и возвращает маску номера"""
    if len(card_number) == 16 and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    elif card_number == '':
        return f'Вы не ввели номер карты'
    else:
        return f'Вы ввели некорректный номер карты'


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает на вход номер счета в виде числа и возвращает маску номера"""
    if len(account_number) == 20 and account_number.isdigit():
        return f"**{account_number[-4:]}"
    elif account_number == '':
        return f'Вы не ввели номер счета'
    else:
        return f'Вы ввели некорректный номер карты'


if __name__ == "__main__": # pragma: no cover
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
