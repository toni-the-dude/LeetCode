class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        max = 0

        for s in sentences:
            l = len(s.split(' '))
            if l > max: max = l 

        return max