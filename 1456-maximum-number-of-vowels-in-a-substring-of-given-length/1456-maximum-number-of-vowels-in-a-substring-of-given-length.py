class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        max_vow = 0
        current_vow = 0
        head = 0
        tail = 0
        
        while head < k:
            if s[head] in "aeiou":
                current_vow += 1
            head += 1
        head -= 1
        max_vow = current_vow
        # print("Current number of vowels:{0}".format(current_vow))
        
        while head < len(s):
            if s[tail] in "aeiou":
                current_vow -= 1
                # print("Lost the vowel {0}".format(s[tail]))
            tail += 1
            head += 1
            # print(tail)
            # print(head)
            if head != len(s):
                # print("It's not the end")
                if s[head] in "aeiou":
                    # print("Gained another")
                    current_vow += 1
                    # print("Gained the vowel {0}".format(s[head]))
                
            if current_vow > max_vow:
                max_vow = current_vow
            # print("Current number of vowels:{0}".format(current_vow))

        
        return max_vow