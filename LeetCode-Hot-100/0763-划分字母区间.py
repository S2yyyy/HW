class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_dict = {}
        for i in range(len(s)):
            if s[i] in char_dict:
                char_dict[s[i]].append(i)
            else:
                char_dict[s[i]] = [i]
        index = []
        for key, value in char_dict.items():
            index.append([value[0],value[-1]])
        index.sort(key = lambda x:x[0])
        merge = [index[0]]
        for i in range(1,len(index)):
            if index[i][0] <= merge[-1][1]:
                merge[-1][1] = max(merge[-1][1], index[i][1])
            else:
                merge.append(index[i])
        ans = []
        for i in merge:
            ans.append(i[1] - i[0] + 1)
        return ans
        
        
