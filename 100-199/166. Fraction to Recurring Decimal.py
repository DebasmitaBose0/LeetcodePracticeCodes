class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []

        # sign
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')

        num = abs(numerator)
        den = abs(denominator)

        # integer part
        res.append(str(num // den))
        remainder = num % den

        if remainder == 0:
            return "".join(res)

        res.append('.')

        seen = {}

        while remainder:
            if remainder in seen:
                idx = seen[remainder]
                res.insert(idx, '(')
                res.append(')')
                break

            seen[remainder] = len(res)

            remainder *= 10
            res.append(str(remainder // den))
            remainder %= den

        return "".join(res)