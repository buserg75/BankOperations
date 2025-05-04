from typing import Any, Dict, List


def filter_by_state(data_list: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """Функция возвращает новый список, отфильтрованный по указанному значению"""
    return [i for i in data_list if i.get("state") == state]


def sort_by_date(data_list: List[Dict[str, Any]], ascending: str = True) -> List[Dict[str, Any]]:
    """Функция возвращает новый список, отсортированный по дате"""
    return sorted(data_list, key=lambda x: x.get("date"), reverse=ascending)
