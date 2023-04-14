class Solution:
    def myAtoi(self, s: str) -> int:
        #remove leading whitespace
        s = s.lstrip()
        #check for sign
        if s and (s[0] == '-' or s[0] == '+'):
            sign = s[0]
            s = s[1:]
        else:
            sign = ''
        #parse digits
        num_str = ''
        for c in s:
            if c.isdigit():
                num_str += c
            else:
                break
        #convert to int and apply sign
        if num_str:
            num = int(sign + num_str)
        else:
            num = 0
        #clamp to range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        elif num > INT_MAX:
            return INT_MAX
        else:
            return num