from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            key = ''.join(sorted(word))  # sorted string as key
            anagram_map[key].append(word)
        
        return list(anagram_map.values())