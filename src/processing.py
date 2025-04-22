from typing import List, Dict, Any

def filter_by_state(data_list: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """Функция возвращает новый список, отфильтрованный по указанному значению"""
    return [i for i in data_list if i.get("state") == state]





