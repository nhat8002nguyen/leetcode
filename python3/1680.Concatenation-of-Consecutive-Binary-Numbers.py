class Solution:
    def concatenatedBinary(self, n: int) -> int:
        concatenate_bin = ""
        for i in range(1, n+1):
            concatenate_bin = concatenate_bin + self.getBinary(i) 

        return self.getDecimal(concatenate_bin)

    def getBinary(self, num: int) -> str: 
        divider = num
        result = ""
        while divider != 0:
            if divider%2 == 1:
                result = "1" + result
            else:
                result = "0" + result

            divider = divider//2

        return result

    def getDecimal(self, binary: str):
        result = 0
        exponential = 0
        for i in range(len(binary)-1, -1, -1):
            num = int(binary[i])
            result += num * pow(2, exponential)
            exponential += 1

        return result

s = Solution()
# print(s.concatenatedBinary(1))
# print(s.concatenatedBinary(3))
print(s.concatenatedBinary(12))