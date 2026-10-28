class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        S = set(nums)
        
        # Step 1: All unique pair XORs
        pairs = {x ^ y for x in S for y in S}
        
        # Step 2: Combine pairs with single elements to get triplet XORs
        triplets = {p ^ z for p in pairs for z in S}
        
        return len(triplets)