# Given a string S which consists of only lowercase English alphabets, you have to perform the below operations:
# If the string S contains any repeating character, remove the first repeating character and reverse the string and again perform the above operation on the modified string, otherwise, you stop.
# You have to find the final string.
class Solution:
    def removeReverse(self, S): 
        #code here
        n = len(S)
        char_count = {}
        for char in S:
            char_count[char] = char_count.get(char, 0) + 1

        left, right = 0, n - 1
        dir = 0
    
        while left <= right:
            if dir == 0:
                if char_count[S[left]] == 1:
                    left += 1
                else:
                    char_count[S[left]] -= 1
                    S = S[:left] + '#' + S[left + 1:]
                    left += 1
                    dir = 1
            else:
                if char_count[S[right]] == 1:
                    right -= 1
                else:
                    char_count[S[right]] -= 1
                    S = S[:right] + '#' + S[right + 1:]
                    right -= 1
                    dir = 0
    
        res = ""
        for char in S:
            if char != '#':
                res += char
    
        if dir == 1:
            res = res[::-1]
    
        return res