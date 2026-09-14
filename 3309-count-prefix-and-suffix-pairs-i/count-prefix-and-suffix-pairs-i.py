class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count  = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                count+= self.isPrefixAndSuffix(words[i],words[j])
        return count
    
    def isPrefixAndSuffix(self,str1,str2):
        m = len(str1)
        if str1 == str2[:m] and str1 == str2[len(str2) - m:]:
            #print(str1, str2[:m], str1 , str2[len(str2) - m:])
            return 1
        else:
            return 0
    

        