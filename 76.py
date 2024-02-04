class Solution:
    # code from prodonik
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        # All the ASCII characters
        map = [0] * 128
        count = len(t)

        # The sliding window
        start = 0
        end = 0
        min_len = float('inf')

        # The final returning window
        start_index = 0

        # Initialize the list, with chars in t
        for char in t:
            map[ord(char)] += 1

        # While the window hasn't reach the end
        while end < len(s):

            # If char in t
            if map[ord(s[end])] > 0:
                count -=1
            map[ord(s[end])] -= 1
            end +=1

            # While the window has all the chars in t
            while count == 0:

                # If a new min is found
                if end-start < min_len:
                    start_index = start
                    min_len = end - start

                # If we give up a char that is in t, we add 1 to count
                if map[ord(s[start])] == 0:
                    count += 1
                # Give up the char
                map[ord(s[start])] += 1
                start += 1
                
        return "" if min_len == float('inf') else s[start_index: start_index + min_len]
        
