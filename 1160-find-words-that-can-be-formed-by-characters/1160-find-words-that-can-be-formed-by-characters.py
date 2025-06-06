class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        dict = {}
        sum = 0

        for c in chars:
            dict[c] = dict.get(c, 0) + 1

        for w in words:
            cpy = dict.copy()
            good = True

            for c in w:
                if c not in cpy.keys() or cpy[c] < 1: 
                    good = False
                    break
                cpy[c] -= 1

            if good == True: sum += len(w)

        return sum