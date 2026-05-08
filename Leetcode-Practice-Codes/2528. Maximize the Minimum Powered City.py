class Solution:
    def maxPower(self, stations, r, k):
        n = len(stations)
        pref = [0] * (n + 1)
        
        for i in range(n):
            pref[i + 1] = pref[i] + stations[i]
        
        power = [0] * n
        for i in range(n):
            l = max(0, i - r)
            rr = min(n - 1, i + r)
            power[i] = pref[rr + 1] - pref[l]
        
        def check(x):
            extra = [0] * (n + 1)
            curr = 0
            used = 0
            
            for i in range(n):
                curr += extra[i]
                if power[i] + curr < x:
                    need = x - (power[i] + curr)
                    used += need
                    if used > k:
                        return False
                    curr += need
                    j = min(n, i + 2 * r + 1)
                    if j < n:
                        extra[j] -= need
            
            return True
        
        l, rr = 0, 10**18
        
        while l < rr:
            mid = (l + rr + 1) // 2
            if check(mid):
                l = mid
            else:
                rr = mid - 1
        
        return l