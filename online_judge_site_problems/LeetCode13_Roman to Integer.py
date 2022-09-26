class Solution:
    def romanToInt(self, s: str) -> int:
        RomanNum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        for i, v in enumerate(s):
            add_value = RomanNum[v]
            if i and v in "VLDXCM":
                if v in "VX" and s[i - 1] == 'I':
                    if v == "V": add_value = (4 - 1)
                    if v == "X": add_value = (9 - 1)

                if v in "LC" and s[i - 1] == 'X':
                    if v == "L": add_value = (40 - 10)
                    if v == "C": add_value = (90 - 10)

                if v in "DM" and s[i - 1] == 'C':
                    if v == "D": add_value = (400 - 100)
                    if v == "M": add_value = (900 - 100)
            sum += add_value
        return sum

sol = Solution()

result = sol.romanToInt("LVIII")

print(result)