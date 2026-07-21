from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for item in strs:
            sorted_item = ''.join(sorted(item))
            print(sorted_item)
            groups[sorted_item].append(item)
        return list(groups.values())