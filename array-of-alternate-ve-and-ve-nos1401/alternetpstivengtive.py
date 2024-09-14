class Solution:
    def rearrange(self,arr):
        neg = []
        pos = []
        for i in arr:
            if i< 0:
                neg.append(i)
            else:
                pos.append(i)
        p = n = a = 0
        nl = len(neg)
        pl = len(pos)
        while nl>n and pl>p:
            arr[a] = pos[p]
            a+= 1
            arr[a] = neg[n]
            a+=1
            n+=1
            p+=1
        while nl>n:
            arr[a] = neg[n]
            a+=1
            n+=1
        while pl>p:
            arr[a] = pos[p]
            a+=1
            p+=1
        