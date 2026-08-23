
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        for i in strs:
            sort_i = "".join(sorted(i))
            check.setdefault(sort_i, []).append(i)
        return list(check.values())
