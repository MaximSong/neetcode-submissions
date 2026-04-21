class Solution:
    def swap(self, start, end, s):
        temp = s[start]
        s[start] = s[end]
        s[end] = temp
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
        while start <= end:
            self.swap(start , end ,s)
            start += 1
            end -= 1
        
        