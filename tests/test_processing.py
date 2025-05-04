from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(data_list, state, data_list_2):
    assert filter_by_state(data_list, state) == data_list_2


def test_filter_by_state_2(data_list, state_2, data_list_3):
    assert filter_by_state(data_list, state_2) == data_list_3


def test_filter_by_state_3(data_list, data_list_2):
    assert filter_by_state(data_list) == data_list_2


def test_filter_by_state_4(data_list_without_state, squares):
    assert filter_by_state(data_list_without_state) == squares


def test_sort_by_date(data_list, data_list_sorted):
    assert sort_by_date(data_list) == data_list_sorted


def test_sort_by_date_2(data_list, data_list_sorted_2):
    assert sort_by_date(data_list, ascending=False) == data_list_sorted_2

