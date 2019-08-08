class square_digits:

    def __init__(self):
        self.num = 0
        self.str_num = ''
        self.num_list = []

    def set_num(self, num):
        self.num = num

    def get_num(self):
        return self.num

    def get_score(self):
        self.str_num = str(self.num)
        for num in self.str_num:
            self.num_list.append(int(num)**2)
        return int(''.join(str(num) for num in self.num_list))

