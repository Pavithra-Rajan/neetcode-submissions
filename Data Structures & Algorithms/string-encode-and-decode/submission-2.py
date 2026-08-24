class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []

        while i < len(s):
            # parse length
            count = 0
            while s[i].isdigit():
                count = count * 10 + int(s[i])
                i += 1

            # skip '#'
            i += 1  

            # extract word
            decoded.append(s[i:i+count])
            i += count

        return decoded
