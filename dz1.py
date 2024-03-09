###
# 1. Доработать класс `FlatIterator` в коде ниже. Должен получиться итератор, который принимает список списков и возвращает их плоское представление,
# т. е. последовательность, состоящую из вложенных элементов. 
# Функция `test` в коде ниже также должна отработать без ошибок.
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.cursor1=0
        self.cursor2=0
        self.count_of_list = len(list_of_list)

    def __iter__(self):
        self.len_of_list = len(self.list_of_list[self.cursor1])
        return self

    def __next__(self):
        if self.cursor2>=self.len_of_list:
            self.cursor1 +=1
            if self.cursor1>=self.count_of_list:
                raise StopIteration
            self.list_new = self.list_of_list[self.cursor1]
            self.len_of_list = len(self.list_new)
            self.cursor2=0
        item = self.list_of_list[self.cursor1][self.cursor2]
        self.cursor2 +=1
        # print(self.cursor1," ", self.cursor2)
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
# list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
# ]
# for item in FlatIterator(list_of_lists_1):
#     print (item)
