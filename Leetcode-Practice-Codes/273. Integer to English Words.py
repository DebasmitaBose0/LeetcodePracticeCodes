class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        self.less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                             "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

        res = ""
        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                res = self.helper(num % 1000) + self.thousands[i] + " " + res
            num //= 1000
            
        return res.strip()

    def helper(self, n: int) -> str:
        if n == 0:
            return ""
        elif n < 20:
            return self.less_than_20[n] + " "
        elif n < 100:
            return self.tens[n // 10] + " " + self.helper(n % 10)
        else:
            return self.less_than_20[n // 100] + " Hundred " + self.helper(n % 100)