class Solution:
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        res = 0
        a = b = -1  # last two picked numbers
        
        for l, r in intervals:
            if l > b:
                # need 2 new numbers
                res += 2
                a, b = r - 1, r
            elif l > a:
                # need 1 more number
                res += 1
                a, b = b, r
        
        return res