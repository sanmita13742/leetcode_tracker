from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        s= ''
        for word in strs:
            s += str(len(word)) + "#" + word
        #print(s)
        return s
       
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i<len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            res.append("".join(s[j+1:j+length+1]))
            i = j + length + 1
        #print(res)

        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))