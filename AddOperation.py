#66. Plus One
class Solution(object):
    def plusOne(self, digits):
        length = len(digits)
        if digits[length-1] != 9:
            digits[length-1] += 1
        else:
            idx = length-1
            
            while idx >= 0:
                if digits[idx] == 9:
                    digits[idx] = 0
                    idx -= 1
                else:
                    digits[idx] += 1
                    break
            if idx<0:
                digits.insert(0,1)
        return digits