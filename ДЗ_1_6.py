class QueueClass:
    def __init__(self):
        self.base = []
        self.finalize = []
        self.finale = []

    def is_empty_base(self):
        return self.base == []

    def is_empty_finalize(self):
        return self.finalize == []   

    def is_empty_finale(self):
        return self.finale == []    

    def to_base_queue(self, item):
        self.base.insert(0, item)

    def solve_base(self, num_of_solved):
        temp = None
        i = 1
        if num_of_solved > len(self.base):
            print('Количество решенных задач больше чем поставлненных! Проверьте условие!')
            return 1
        while i <= num_of_solved:
            temp = self.base.pop()
            print("Задача", temp, " отправлена на доработку")
            self.finalize.insert(0, temp)
            i += 1
    
    def check_finalize(self, num_checked):
        temp = None
        i = 1
        if num_checked > len(self.finalize):
            print('Количество доработанных задач больше чем поставлненных! Проверьте условие!')
            return 1
        while i <= num_checked:
            temp = self.finalize.pop()
            print('Задача', temp, "была выполнена и проверена")
            self.finale.insert(0, temp)
            i += 1

    def from_finale(self):
        return self.finale.pop()

    def size_of_base(self):
        return len(self.base)

    def size_of_finalize(self):
        return len(self.finalize) 

    def size_of_finale(self):
        return len(self.finale)  


test_object = QueueClass()
test_object.to_base_queue('1_item')
test_object.to_base_queue('2_item')
test_object.to_base_queue('3_item')
print("Длина базовой очереди после 3 задач:", test_object.size_of_base())
test_object.solve_base(2)
test_object.check_finalize(1)
