class Solution:
    def encode(self, strs: List[str]) -> str:
        # Encode format: [length][#][string]
        # Example: ["abc", "def"] -> "3#abc3#def"
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Find the next delimiter '#'
            j = i
            while s[j] != '#':
                j += 1
            
            # The length of the next string is between i and j
            length = int(s[i:j])
            
            # Move the pointer past the '#'
            i = j + 1
            
            # Extract the actual string using the length
            res.append(s[i : i + length])
            
            # Move the pointer to the start of the next encoded string
            i += length
            
        return res