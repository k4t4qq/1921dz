class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        self.i += 1
        def baza(text):
            i = "a"
            while True:
                text_1 = str(text)+i
                yield text_1
                if len(text_1) > 5:
                    return
                i = str(i)+"a"
        ok = baza("a")
        print(ok)
        for _ in ok:
            print(_)
        if self.i > self.max_number:
            raise StopIteration
        return self.i
count = Counter(5)
for elem in count:
    print(elem)
