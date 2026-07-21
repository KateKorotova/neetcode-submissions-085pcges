class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return '[]'
        len_lst = []
        for i in strs:
            len_lst.append(str(len(i)))
        len_str = ','.join(len_lst)
        joined_strs = ''.join(strs)
        return '#'.join([len_str, joined_strs])

    def decode(self, s: str) -> List[str]:
        if s is '[]':
            return []
        res = []
        i_shrp = s.find('#')
        len_str = s[:i_shrp].split(',')
        strs = s[i_shrp+1:]
        global_count = 0
        for count in len_str:
            c = int(count)
            res.append(strs[global_count:global_count+c])
            global_count += c
        return res
            


