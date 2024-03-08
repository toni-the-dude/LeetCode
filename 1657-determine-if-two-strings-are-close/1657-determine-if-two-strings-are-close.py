# Operation 1 implies that the frequency of the involved characters should be equal, i.e. fr1[letter] = fr2[letter]
# Operation 2 implies that for any mismatched frequency, there should be another character with a matching frequency, such that fr1[letter1] = fr2[letter2].
# No character should be left without a match
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False
        
        fr1 = {}
        fr2 = {}
        
        for char in word1:
            if char not in fr1.keys():
                fr1[char] = 1
            else:
                fr1[char] += 1
                
        for char in word2:
            if char not in fr2.keys():
                fr2[char] = 1
            else:
                fr2[char] += 1                
        
        fr3 = [[],[]] # Stores mismatched keys
        for k, v in fr1.items():
            if k in fr2.keys():
                if v == fr2[k]:
                    fr2.pop(k, None)
                else: # Failed to qualify for operation 1, might qualify for operation 2
                    fr3[0].append(k)
                    fr3[1].append(k)
            else:
                return False
        print(fr3)
        pair = False
        while len(fr3[0]) != 0:
            pair = False
            for j in range(0, len(fr3[1]), 1):
                if fr1[fr3[0][0]] == fr2[fr3[1][j]]:
                    fr3[0].pop(0)
                    fr3[1].pop(j)
                    print(fr3)
                    pair = True
                    break
            if pair == False:
                return False
        
        if fr3 == [[],[]]:
            return True
        
        return False