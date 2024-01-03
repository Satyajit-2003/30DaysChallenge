# Maintain a virtual queue of size k
# key is the last index where the num is not equal to the value
# if key is les than or equals 0, then we have k consecutive numbers

class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.val = value
        self.key = k

    def consec(self, num: int) -> bool:
        if num != self.val:
            self.key = self.k
            return False
        self.key -= 1
        if self.key <= 0:
            return True
        return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)