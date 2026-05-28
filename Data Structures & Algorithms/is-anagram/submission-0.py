class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = defaultdict(int)

        for char in s:
            hashmap[char] += 1
        
        for char in t:
            hashmap[char] -= 1

        return all(x == 0 for x in hashmap.values())