class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """
        li=[]
        rem=0
        while(n!=0):
            rem=n%10
            li.append(rem)
            n=n/10
        DigitSum=0
        SSum=0
        for i in li:
            DigitSum+=i
            SSum=SSum+(i**2)
        if (SSum-DigitSum)>=50:
            return True
        else:
            return False
