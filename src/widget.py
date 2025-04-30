from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_numbers: str) -> str:
    """Функция, которая принимает на вход строку, содержащую тип и номер карты или счета,
    и возвращает строку с замаскированным номером"""
    if type_numbers == '':
        return f'Вы не ввели номер карты или счета'
    account_name, account_number = type_numbers.rsplit(' ', maxsplit=1)
    if account_name == 'Счет' and len(account_number) == 20:
        masked_account_number = get_mask_account(account_number)
    elif len(account_number) < 16 or len(account_number) > 16:
        return f'Вы ввели некорректные данные'
    else:
        masked_account_number = get_mask_card_number(account_number)
    return f'{account_name} {masked_account_number}'


def get_date(date_string: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    if date_string == '' or len(date_string) != 26:
        return f'Вы ввели некорректную дату'
    else:
        date_list = date_string[:10].split("-")[::-1]
        return ".".join(date_list)

