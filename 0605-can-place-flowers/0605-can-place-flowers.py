class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        if n == 0: return True

        if len(flowerbed) == 1:
            if n == 1 and flowerbed[0] == 0: return True
            return False

        for index in range(len(flowerbed)):

            if index == 0:
                if flowerbed[index] == 0 and flowerbed[index + 1] == 0:
                    flowerbed[index] = 1
                    n -= 1

            elif index == (len(flowerbed) - 1):
                if flowerbed[index] == 0 and flowerbed[index - 1] == 0:
                    flowerbed[index] = 1
                    n -= 1

            elif flowerbed[index] == 0 and flowerbed[index - 1] == 0 and flowerbed[index + 1] == 0:
                flowerbed[index] = 1
                n -= 1

            if n == 0: return True
            
        return False