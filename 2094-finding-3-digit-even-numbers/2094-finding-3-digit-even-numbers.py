class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = {}
        output = set()

        for digit in digits:
            freq[digit] = freq.get(digit, 0) + 1

        for d1 in range(1, 10):
            if freq.get(d1, 0) == 0:
                continue
            freq1 = freq.copy()
            freq1[d1] -= 1

            for d2 in range(0, 10):  # tens digit
                if freq1.get(d2, 0) == 0:
                    continue
                freq2 = freq1.copy()
                freq2[d2] -= 1

                for d3 in range(0, 10, 2):  # units digit: must be even
                    if freq2.get(d3, 0) == 0:
                        continue
                    number = d1 * 100 + d2 * 10 + d3
                    output.add(number)

        return sorted(output)