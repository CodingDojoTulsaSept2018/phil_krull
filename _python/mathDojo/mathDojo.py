class MathDojo(object):

    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        print(type(nums))
        # print(len(nums))
        self.result += num
        for val in nums:
            self.result += val
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for val in nums:
            self.result -= val
        return self

md = MathDojo()

# print(md)

# md1 = MathDojo()
# md1.result += 5
value = 9
x = md.add(2,5,1,7,8,9).subtract(3,2.8).add(value).result
print(x) # should print 5
# print(md1.result)
