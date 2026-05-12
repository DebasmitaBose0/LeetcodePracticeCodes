class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Sort the scores in descending order
        # We keep track of the original index using sorted() and enumerate
        sorted_scores = sorted(score, reverse=True)
        
        # Create a mapping of score -> rank
        rank_map = {}
        for i, s in enumerate(sorted_scores):
            if i == 0:
                rank_map[s] = "Gold Medal"
            elif i == 1:
                rank_map[s] = "Silver Medal"
            elif i == 2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(i + 1)
        
        # Build the result array based on the original score order
        return [rank_map[s] for s in score]