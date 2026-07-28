class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=2:
            return s
            
        n=len(s)//2
        m=""
        if len(s)%2==1:
            m+=s[n]

        res=sorted(s[:n])
        f="".join(res)

        return f+m+f[::-1]
            
            