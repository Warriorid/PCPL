class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.seen = set()
        self.ignore_case = kwargs.get('ignore_case', False)

    def __next__(self):
        while True:
            try:
                item = next(self.items)
            except StopIteration:
                raise StopIteration
            
            if self.ignore_case:
                item = item.lower()
            
            if item not in self.seen:
                self.seen.add(item)
                return item

    def __iter__(self):
        return self

data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
for item in Unique(data):
    print(item)

data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
for i in Unique(data, ignore_case = True):
    print(i)

