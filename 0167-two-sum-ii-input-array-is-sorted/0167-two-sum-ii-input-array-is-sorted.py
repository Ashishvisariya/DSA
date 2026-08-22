class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers)-1
        s = True
        while s:
            if numbers[i] + numbers[j] > target:
                j-=1
            elif target > numbers[i] + numbers[j]:
                i+=1
            if numbers[i] + numbers[j] == target:
                s = False
                return [i+1,j+1]
        return -1

        
        
