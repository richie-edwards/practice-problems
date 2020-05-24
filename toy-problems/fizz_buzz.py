class Solution:
    def __init__(self):
        pass

    def is_multiple(self, num, multiple):
        return (num % multiple) == 0

    def fizz_buzz(self):
        for i in range(1, 101):
            if self.is_multiple(i, 3) and self.is_multiple(i, 5):
                print("FizzBuzz")
            elif self.is_multiple(i, 3):
                print("Fizz")
            elif self.is_multiple(i, 5):
                print("Buzz")
            else:
                print(i)


test = Solution()
test.fizz_buzz()
