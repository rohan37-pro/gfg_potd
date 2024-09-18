class Solution:
    def ispar(self,x):
        parVal = {'(':1, ')':1, '{':2, '}':2, '[':3, ']':3}
        exp = []
        for i in x:
            if i in '([{':
                exp.append(i)
            else:
                if exp==[]:
                    return False
                if parVal[i]==parVal[exp[-1]]:
                    exp = exp[:-1]
                else:
                    return False
        if exp==[]:
            return True
        else:
            return False