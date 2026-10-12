class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapp = {}
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i in range(len(s)):
            if pattern[i] in mapp:
                if mapp[pattern[i]] != s[i]:
                    return False
            else:
                mapp[pattern[i]] = s[i]
        if len(set(mapp.values())) != len(mapp.values()):
            return False
        return True









        












        














