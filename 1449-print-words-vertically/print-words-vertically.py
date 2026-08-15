class Solution:
    def printVertically(self, s: str) -> List[str]:
        ans = []
        sList = s.split()
        maxstr= max(sList,key=len)
        print(maxstr)
        maxlen=len(maxstr)
        for i in range(maxlen):
            element=[]
            for word in sList:
                if len(word)> i:
                    element.append(word[i])
                else:
                    element.append(' ')
            ans.append("".join(element).rstrip())
        return ans
        
                
            