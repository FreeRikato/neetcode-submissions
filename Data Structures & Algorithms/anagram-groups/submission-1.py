from collections import defaultdict
class Solution:
    def prime(self, num: int) -> bool:
        if num < 2: return False

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0: return False

        return True

    def getFirst26Prime(self) -> List[int]:
        count = 0
        tracer = 2
        prime_numbers = []
        while(len(prime_numbers) < 27):
            if self.prime(tracer):
                count += 1
                prime_numbers.append(tracer)
            tracer += 1
        return prime_numbers

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prime_numbers = self.getFirst26Prime()
        hashmap = defaultdict(list)

        for s in strs:
            primeMultiple = 1
            for char in s.lower():
                primeMultiple = primeMultiple * prime_numbers[ord(char) - ord('a')]

            hashmap[primeMultiple].append(s)

        return list(hashmap.values())