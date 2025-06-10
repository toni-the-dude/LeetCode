class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        output = []

        for i in range(0, len(words), 1):

            if x in words[i]:

                output.append(i)

        return output