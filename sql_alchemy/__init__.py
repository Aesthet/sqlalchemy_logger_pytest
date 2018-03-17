import math


class MyRange:
    def __init__(self, begin, end=None, step=1):
        if end is None:
            self.start = 0
            self.finish = begin
        else:
            self.start = begin
            self.finish = end

        if step != 0:
            self.step = step
        else:
            raise ValueError("Invalid step value. Step cannot be zero")

        self.length = math.ceil((self.finish - self.start) / self.step)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if 0 <= index < len(self):
            return self.start + index * self.step
        else:
            raise IndexError("Index out of range")

    def __repr__(self):
        return "MyRange({}, {}, {})".format(self.start, self.finish, self.step)


def my_for(iterable):
    FOR_iterator = iter(iterable)

    while True:
        try:
            print(next(FOR_iterator))
        except StopIteration:
            break


my_for(MyRange(10, -3, -4))