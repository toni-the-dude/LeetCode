class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        arr = [first]

        for is_xored in encoded:
            arr.append(arr[-1] ^ is_xored)

        return arr