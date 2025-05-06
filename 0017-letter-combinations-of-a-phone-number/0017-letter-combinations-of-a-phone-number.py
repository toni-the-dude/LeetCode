from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "": return []

        phone_keypad = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        letters = [phone_keypad[d] for d in digits]

        return [''.join(p) for p in product(*letters)]