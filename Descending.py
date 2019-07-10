class Descending:

    def __init__(self):
        self.num = 0
        self.vlist = []

    def get_value(self, param):
        self.num = param
        value = str(self.num)
        for number in value:
            self.vlist.append(number)
        self.vlist.reverse()
        return int(''.join(self.vlist))
