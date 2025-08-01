class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.split(" ")

        for i, w in enumerate(s):
            s[i] = w[::-1]

        return " ".join(s)