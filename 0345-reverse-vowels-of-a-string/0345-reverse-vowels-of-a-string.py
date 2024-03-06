class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        start_index = 0
        end_index = len(s) - 1
        start_is_vowel = False
        end_is_vowel = False
        s_list = list(s)

        while start_index < end_index:

            if s_list[start_index].lower() not in "aeiou":
                start_index += 1
            else: start_is_vowel = True

            if s_list[end_index].lower() not in "aeiou":
                end_index -= 1
            else: end_is_vowel = True

            if start_is_vowel is True and end_is_vowel is True:
                aux = s[start_index]
                s_list[start_index] = s_list[end_index]
                s_list[end_index] = aux
                start_index += 1
                end_index -= 1
                start_is_vowel = False
                end_is_vowel = False
        new_s = "".join(s_list)
        return new_s
            