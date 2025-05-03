class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        s1 = "qwertyuiop"
        s2 = "asdfghjkl"
        s3 = "zxcvbnm"
        result = []

        for word in words:
            if all(c.lower() in s1 for c in word) or all(c.lower() in s2 for c in word) or all(c.lower() in s3 for c in word): result.append(word)

        return result