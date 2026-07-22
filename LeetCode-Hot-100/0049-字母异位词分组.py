class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict={}
        for i in strs:
            re="".join(sorted(i))
            if re in strs_dict:
                strs_dict[re].append(i)
            else:
                strs_dict[re]=[i]
        
        return list(strs_dict.values())
