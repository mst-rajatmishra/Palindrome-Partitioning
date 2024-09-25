from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        def backtrack(start: int, path: List[str]):
            # If we've reached the end of the string, add the current path to the result
            if start == len(s):
                result.append(path.copy())
                return
            
            # Explore all substrings starting from 'start'
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)  # Choose the substring
                    backtrack(end, path)     # Explore further
                    path.pop()               # Backtrack
        
        result = []
        backtrack(0, [])
        return result
