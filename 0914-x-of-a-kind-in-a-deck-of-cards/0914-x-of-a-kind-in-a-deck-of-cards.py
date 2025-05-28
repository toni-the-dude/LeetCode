class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        freq = {}

        for card in deck:
            freq[card] = freq.get(card, 0) + 1

        min = pow(10, 4)

        for nr in freq.values():
            if nr > 1:
                if nr < min: min = nr
            else: return False

        for i in range(2, min + 1, 1):
            found_common_div = True
            for nr in freq.values():
                if nr % i != 0: found_common_div = False
            if found_common_div == True: return True

        return False