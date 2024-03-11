# 2. Доработать функцию flat_generator. Должен получиться генератор,
# который принимает список списков и возвращает их плоское представление.
# Функция `test` в коде ниже также должна отработать без ошибок.
# ```python
import types


def flat_generator(list_of_lists):
    for list in list_of_lists:
        for item in list:
            yield item



def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
result_ = list(flat_generator(list_of_lists=list_of_lists_1))
print(result_)