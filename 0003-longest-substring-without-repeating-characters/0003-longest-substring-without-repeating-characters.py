class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        seen_chars = set()
        max_length = 0

        while right < len(s):
            if s[right] not in seen_chars:
                seen_chars.add(s[right])
                right += 1
                max_length = max(max_length, right - left)
            else:
                seen_chars.remove(s[left])
                left += 1

        return max_length

                