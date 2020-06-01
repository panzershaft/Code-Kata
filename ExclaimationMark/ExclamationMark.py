"""
 Each exclamation mark weight is 2; Each question mark weight is 3. Put two string left and right to the balance, Are they balanced?

If the left side is more heavy, return "Left"; If the right side is more heavy, return "Right"; If they are balanced, return "Balance".
Examples

balance("!!","??") == "Right"
balance("!??","?!!") == "Left"
balance("!?!!","?!?") == "Left"
balance("!!???!????","??!!?!!!!!!!") == "Balance"
"""


class Balance:

    def __init__(self):
        self.left = ''
        self.right = ''

    def set_values(self, left, right):
        self.left = left
        self.right = right

    def get_score(self):
        left_weight = self.left.count('!') * 2 + \
                      self.left.count('?') * 3
        right_weight = \
            self.right.count('!') * 2 + \
            self.right.count('?') * 3
        if right_weight > left_weight:
            return "Right"
        elif left_weight > right_weight:
            return "Left"
        else:
            return "Balance"

