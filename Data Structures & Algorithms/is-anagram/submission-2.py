class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp_s = {}
        mp_t = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            mp_s[s[i]] = mp_s.get(s[i] , 0) + 1
            mp_t[t[i]] = mp_t.get(t[i] , 0) + 1
        if mp_s != mp_t:
            return False
        return True