class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,str):
        return ".".join(str.split(".")[-1::-1])