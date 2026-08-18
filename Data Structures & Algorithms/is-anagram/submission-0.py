class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = {}
        for i in s:
            if i not in check:
                check[i] = 1
            else: 
                check[i] += 1
        
        for i in t:
            if i not in check:
                check[i] = 1
            else: 
                check[i] -= 1
            if check[i] == 0:
                del check[i]
        
        if not check:
            return True

        else: 
            return False