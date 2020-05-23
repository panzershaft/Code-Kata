class Bowling:
    def __init__(self):
        self.rolls = []

    def roller(self, pins, throws):
        for throw in range(throws):
            self.rolls.append(pins)

    def get_score(self):
        score = 0
        index = 0
        for frame_index in range(10):
            if self.spare(index):
                score += self.spare_score(index)
                index += 2
            elif self.strike(index):
                score += self.strike_score(index)
                index += 1
            else:
                score += self.normal_score(index)
                index += 2
        return score

    def normal_score(self, index):
        return self.rolls[index] + self.rolls[index + 1]

    def spare(self, index):
        return self.rolls[index] + self.rolls[index + 1] == 10

    def spare_score(self, index):
        return 10 + self.rolls[index + 2]

    def strike(self, index):
        return self.rolls[index] == 10

    def strike_score(self, index):
        return 10 + self.rolls[index + 1] + self.rolls[index + 2]