class CycleIterator:
    '''
    Пседво-итератор, так как не реализован метод __iter__,
    а метод next без обработки исключения StopIteration.
    '''
    def __init__(self, l):
        self.l = l
        self.index = 0

    def next(self):
        result = self.l[self.index]
        self.index = (self.index + 1) % len(self.l)
        return result

    def prev(self):
        result = self.l[self.index - 1]
        self.index = (self.index - 1) % len(self.l)
        return result
