class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}
        for i in range(len(strs)):
            temp = tuple(sorted(strs[i]))
            if temp not in dicts:
                dicts[temp] = [i]
            else:
                dicts[temp].append(i)
                
        dvs = list(dicts.values())
        result = []
        for data in dvs:
            tmp = []
            for idx in data:
                tmp.append(strs[idx])
            result.append(tmp)
            
        return result