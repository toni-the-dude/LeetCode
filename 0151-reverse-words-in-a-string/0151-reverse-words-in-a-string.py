class Solution:
    def reverseWords(self, s: str) -> str:

        words = []

        words = s.split()

        begin = 0
        end = len(words) - 1

        while begin < end:
            words[begin], words[end] = words[end], words[begin]
            begin += 1
            end -= 1

        answer = " ".join(words)

        return answer