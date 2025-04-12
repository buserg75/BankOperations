from masks import get_mask_card_number, get_mask_account

def mask_account_card(type_numbers: str) -> str:
    """Функция, которая принимает на вход строку, содержащую тип и номер карты или счета,
    и возвращает строку с замаскированным номером"""
    type_numbers_list = type_numbers.split()
    type = []
    numbers = ''
    for i in type_numbers_list:
        if 'Счет' in i:
            return f"Счет {get_mask_account(type_numbers_list[1])}"
        elif i.isalpha():
            type.append(i)
        else:
            numbers += i
            return f"{' '.join(type)} {get_mask_card_number(numbers)}"


def get_date(date_string: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    date_list = date_string[:10].split('-')[::-1]
    return '.'.join(date_list)

