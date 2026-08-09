class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            word = "".join(sorted(s))
            anagram_map[word].append(s)
        return list(anagram_map.values())
            