class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()  # To track characters in the current substring
        count = 1  # We start with at least one substring

        for char in s:
            if char in seen:
                count += 1  # We need a new substring
                seen.clear()  # Reset the set for the new substring
            seen.add(char)

        return count
