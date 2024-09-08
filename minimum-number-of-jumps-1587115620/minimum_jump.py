class Solution:
    def minJumps(self, arr):
        end = len(arr) -1 
        jump_count = 0
        pointer = 0
        jump = arr[0]
        while pointer!=end:
            if jump==0:
                return -1
            if pointer + jump >= end:
                return jump_count + 1
            rd = 0
            mxdis = 0
            mxi = pointer
            for i in range(pointer+1, pointer+jump+1):
                if mxdis < arr[i] +rd:
                    mxdis = arr[i]+rd
                    mxi = i
                rd += 1
            if mxi==pointer:
                return -1
            else:
                jump_count+=1
                pointer=mxi
                jump = arr[mxi]

        return jump_count
