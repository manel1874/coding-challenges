"""
Determine whether a string is a palindrome, ignoring non-alphanumeric characters and case. Examples:

Input: Do geese see God? Output: True

Input: Was it a car or a cat I saw? Output: True

Input: A brown fox jumping over Output: False
"""
import re


class Solution:
    def is_palindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s) - 1
        is_palindrome = True

        while i < j:
            if s[i] == " ":
                i += 1
            if s[j] == " ":
                j -= 1
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return is_palindrome
    

    def is_palindrome_short_solution(self, s: str) -> bool:
        # keep only alphanumeric characters and make them lowercase
        cleaned = re.sub(r'[^a-z0-9]', '', s.lower())
        # check if cleaned string equals its reverse
        return cleaned == cleaned[::-1]
    
    def is_palindrome_ans(s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            # move left pointer until it's alphanumeric
            while l < r and not s[l].isalnum():
                l += 1
            # move right pointer until it's alphanumeric
            while l < r and not s[r].isalnum():
                r -= 1
            
            # compare lowercase versions
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True
    

if __name__ == "__main__":
    first_palind_string = "Do geese see God"
    second_palind_string = "Was it a car or a cat I saw"
    no_palind_string = "A brown fox jumping over"
    is_first_palind_string = Solution().is_palindrome(first_palind_string)
    is_second_palind_string = Solution().is_palindrome(second_palind_string)
    is_no_palind_string = Solution().is_palindrome(no_palind_string)
    print("Input: " + first_palind_string + "." + " Output: " + str(is_first_palind_string))
    print("Input: " + second_palind_string + "." + " Output: " + str(is_second_palind_string))
    print("Input: " + no_palind_string + "." + " Output: " + str(is_no_palind_string))
