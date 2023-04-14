class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                sum = mul + res[p2]
                res[p1] += sum // 10
                res[p2] = sum % 10
        res_str = "".join(map(str, res)).lstrip("0")
        return res_str if res_str else "0"