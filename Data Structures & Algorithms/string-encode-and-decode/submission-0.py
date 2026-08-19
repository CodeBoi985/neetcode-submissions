class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        # Move j forward until you hit #
        while i < len(s):
            j = i
            while s[j] != "#" :
                j += 1
            
            # append word to result
            length_word = int(s[i:j])
            start = j + 1
            end = start + length_word
            my_word = s[start:end]
            res.append(my_word)
            
            # move pointer i to end of word
            i = end
        return res