class Solution:
    def encode(self, strs):
        # write your code here
        encoded_str = ""
        for words in strs:
            temp_len = len(words)
            encoded_str += str(temp_len) + "#" + words

        return encoded_str

    def decode(self, str):
        # write your code here
        res, i = [], 0
        while i != len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = length + j + 1
        return res
