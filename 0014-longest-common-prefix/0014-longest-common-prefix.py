class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
    # Assume the first string is the prefix
        prefix = strs[0]
    
        for word in strs[1:]:
        # Shrink prefix until it matches the start of the current word
            while word[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
    
        return prefix