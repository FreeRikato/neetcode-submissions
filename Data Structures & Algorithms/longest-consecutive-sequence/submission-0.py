class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []: return 0

        setNums = set(nums)
        maximumSequence = 0
        i = 0
        for num in setNums:
            adder = 1
            sequenceLength = 1
            if num - 1 not in setNums:
                while num + adder in setNums:
                    sequenceLength += 1
                    adder += 1
            if sequenceLength > maximumSequence: maximumSequence = sequenceLength

        return maximumSequence
