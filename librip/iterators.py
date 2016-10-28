# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.ind = 0
        self.unique_items = []
        self.items=items
        self.items = iter(self.items)
        self.ignore_case = 'ignore_case' in kwargs.keys() and kwargs['ignore_case'] is True

    def __next__(self):
        while True:
            a = next(self.items)
            b = str(a)
            if self.ignore_case is True:
                b = b.lower()
            if b not in self.unique_items:
                self.unique_items.append(b)
                return a

    def __iter__(self):
        return self
