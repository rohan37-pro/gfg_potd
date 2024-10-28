class Solution:
    def removeDuplicates(self, arr):
        a = []
        for i in arr:
            if i not in a:
                a.append(i)
        return a