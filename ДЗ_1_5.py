
class StackClass:
    def __init__(self):
        self.elems = []
        self.list_of_elems = []
        self.v = None

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems) == 2:
            print('Stack переполнен. Используйте функцию push_max')
            return 0
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)
    
    def push_max(self, el):
        self.v = StackClass()
        self.v.push_in(el)
        return self.v

test = StackClass()
test.push_in(1)
test.push_in(2)
test.push_in(3)
test_2 = test.push_max(3)
print('Верхняя тарелка из test:', test.get_val())
print('Верхняя тарелка из test_2 после push_max:', test_2.get_val())
test_2.push_in(4)
print('Верхняя тарелка из test_2 после push_in:', test_2.get_val())
