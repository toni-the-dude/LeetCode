class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = {}

        w1 = words[0]

        for c in w1:
            freq[c] = freq.get(c, 0) + 1

        for w in words[1:]:
            for k in list(freq.keys()):
                count_in_word = w.count(k)
                if count_in_word == 0:
                    del freq[k]
                else:
                    freq[k] = min(freq[k], count_in_word)

            if len(freq) == 0:
                return []

        answer = []

        for k, v in freq.items():
            while v != 0:
                answer.append(k)
                v -= 1 

        return answer
