class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict by length, and 
        # dict key -> sorting list
        dicts = {}
        for i in range(len(strs)):
            temp = tuple(sorted(strs[i]))
            print(temp)
            if temp not in dicts.keys():
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