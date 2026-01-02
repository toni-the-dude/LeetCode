import numpy as np

class Solution:
    def reverse(self, x: np.int32) -> np.int32:

        if x == 0: return 0

        if x is np.int32(-1 * pow(2, 31)): return 0

        reversed = np.int32(0)
        is_negative = (x < 0)
        x = abs(np.int32(x))

        while x % 10 == 0: x = np.int32(x // 10)

        while x >= 10:
            reversed = np.int32(reversed * 10 + x % 10)
            x = np.int32(x // 10)

        if reversed > np.int32(pow(2, 31) - 1 - x) // 10: return 0

        reversed = np.int32(reversed * 10 + x) 

        if is_negative is True: return np.int32(reversed * -1)

        return reversed