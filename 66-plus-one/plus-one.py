class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        word = ""
        for n in digits:
            word += str(n)
        num = int(word)
        num+=1
        s = str(num)
        ans = []
        for n in s:
            ans.append(int(n))
        return ans
