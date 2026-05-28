class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result = str(len(s)) + "#" + s + result
        return result

    def decode(self, s: str) -> List[str]:
        lengthOfString = len(s)
        i = 0
        result = []
        while i < lengthOfString:
            digit = ""
            while(s[i].isdigit()):
                digit = digit + s[i]
                i += 1

            if s[i] == "#":
                result.append(s[i+1:i+int(digit)+1])

            i += int(digit) + 1
        return result[::-1]
