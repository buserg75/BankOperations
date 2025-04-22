def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает на вход номер карты в виде числа и возвращает маску номера"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает на вход номер счета в виде числа и возвращает маску номера"""
    return f"**{account_number[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
