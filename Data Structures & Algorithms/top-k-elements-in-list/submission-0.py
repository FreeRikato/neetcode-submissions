class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
            Bucket Sort:
            1. Get the hashmap of frequence to each value in nums
            2. Measure the number of unique elements and intialize the bucket list array
            3. Map the frequency hashmap with appropriate index in the bucket list
            4. Traverse the bucket list and append top k frequent elements in result array
        '''
        hashmap = Counter(nums)

        print(f"{hashmap=}")

        numberOfUniqueElements = max(hashmap.values())
        print(f"{numberOfUniqueElements=}")
        bucketList = [[] for _ in range(numberOfUniqueElements)]

        print(f"{bucketList=}")

        for key, value in hashmap.items():
            bucketList[value-1].append(key)

        print(f"{bucketList=}")

        result = []

        for i in range(numberOfUniqueElements - 1, -1, -1):
            frequencyList = bucketList[i]
            for j in range(len(frequencyList)):
                if(len(result) != k):
                    result.append(frequencyList[j])
        return result
