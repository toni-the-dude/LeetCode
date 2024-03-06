class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged_word = ""
        index1 = 0
        index2 = 0

        while index1 < len(word1) and index2 < len(word2):
            merged_word += (word1[index1])
            merged_word += (word2[index2])
            index1 += 1
            index2 += 1

        if len(word1) == len(word2): return merged_word
        elif len(word1) > len(word2): return merged_word + word1[index1:]
        else: return merged_word + word2[index2:]