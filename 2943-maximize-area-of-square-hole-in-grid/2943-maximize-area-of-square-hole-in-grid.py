class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        hSeq = maxhSeq = 1
        vSeq = maxvSeq = 1

        hBars.sort()
        vBars.sort()

        # print(hBars)
        # print(vBars)

        for i in range(1, len(hBars), 1):
            if hBars[i] == hBars[i - 1] + 1: hSeq += 1
            elif hSeq > maxhSeq: 
                maxhSeq = hSeq
                hSeq = 1
            else: hSeq = 1

        for i in range(1, len(vBars), 1):
            if vBars[i] == vBars[i - 1] + 1: vSeq += 1
            elif vSeq > maxvSeq: 
                maxvSeq = vSeq
                vSeq = 1
            else: vSeq = 1


        if hSeq > maxhSeq: 
            maxhSeq = hSeq

        if vSeq > maxvSeq: 
            maxvSeq = vSeq

        # print(maxhSeq, maxvSeq)
        # print(min(maxhSeq, maxvSeq))
        return (min(maxhSeq, maxvSeq) + 1) ** 2