
class Stack:
    def __init__(self,items=[]) -> None:
        self.items = list(items)
        pass

    def is_empty(self):
        """проверка стека на пустоту. Метод возвращает True или False."""
        return not bool(self.items)

    def push(self,item):
        """добавляет новый элемент на вершину стека. Метод ничего не возвращает."""
        self.items.append(item)

    def pop(self):
        """удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека"""
        if self.is_empty():
            raise Exception('Стек пуст')

        return self.items.pop()

    def peek(self):
        """возвращает верхний элемент стека, но не удаляет его. Стек не меняется."""
        if self.is_empty():
            raise Exception('Стек пуст')
        
        return self.items[-1]

    def size (self):
        """возвращает количество элементов в стеке."""
        return len(self.items)

if __name__ == '__main__':
    print(sorted('(((([{}]))))'))
