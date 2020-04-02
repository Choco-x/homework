class udp_check:
    content1 = 0b0110011001100000
    content2 = 0b0101010101010101
    content3 = 0b1000111100001100

    def add(self, x, y):
        res = x + y
        #res = 0b11000000000000001
        while res & (1 << 16) > 0:
            res = (res % 0B10000000000000000) + (res >> 16)
        return res
    def bit_inverse(self):
        res = self.add(self.content1 , self.content2)
        res = self.add(res, self.content3)
        res = self.add(res, ~res + 0b10000000000000000)
        return res



check = udp_check()
print(check.bit_inverse())
# 为什么要用这个画图的库呢？