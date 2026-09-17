class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        for s_letter in s:
            if s_letter in s_hash:
                s_hash[s_letter] = s_hash[s_letter] + 1
            else:
                s_hash[s_letter] = 1
        for t_letter in t:
            if t_letter in s_hash:
                if s_hash[t_letter] - 1 < 0:
                    return False
                s_hash[t_letter] = s_hash[t_letter] - 1
            else:
                return False
        for value in s_hash.values():
            if value != 0:
                return False
        return True
        

        