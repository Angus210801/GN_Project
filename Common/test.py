
class TwoSum(object):
    def __init__(self):
        self.numbers = []

    def add(self, num):
        self.numbers.append(num)

    def find(self, desiredSum):
        for nums in itertools.combinations(self.numbers, 2):
            if sum(nums) == desiredSum:
                return True
        return False


test = TwoSum()
test.add(1)
test.add(3)
test.add(5)
print(test.find(4))
print(test.find(7))
#True
#False