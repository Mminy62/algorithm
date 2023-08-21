class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = collections.defaultdict(list)
        
        for i in range(len(strs)):
            dicts[''.join(sorted(strs[i]))].append(strs[i])
        
        return list(dicts.values())