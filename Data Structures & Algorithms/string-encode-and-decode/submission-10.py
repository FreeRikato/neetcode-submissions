class Solution:
    def encode(self, strs: List[str]) -> str:
        # Lets traverse the list
        encoded_string = ""
        for s in strs:
            # Length of word n + word n + Length of word (n+1) + word (n+1) + ...
            encoded_string = encoded_string + str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        # Traverse through the string
        print(s)
        i = 0
        while i < len(s):
            # Extract length of the string to extract from
            print(i,":")
            length_of_string = 0
            while s[i].isdigit():
                length_of_string = length_of_string*10 + int(s[i])
                i+=1
            extracted_string = (s[i+1 : i + length_of_string+1])
            decoded_string.append(extracted_string)
            i = length_of_string + 1 + i

        print(decoded_string)
        return decoded_string
