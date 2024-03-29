class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Instead of a two-pointer solution I suspected that, in exchange for memory, a hash map might be faster
        dictionary = {}
        answer = 0
        
        for num in nums:
            try:
                dictionary[num] += 1
            except KeyError:
                dictionary[num] = 1
        print(dictionary)
        
        for key, value in dictionary.items():
            if (k - key) in dictionary.keys():
                while dictionary[key] != 0:
                    
                    if key == (k - key) and dictionary[key] != 1:
                        dictionary[key] -= 2
                        answer += 1
                        continue
                        
                    if key == (k - key) and dictionary[key] == 1:
                        dictionary[key] -= 1
                        continue
                        
                    if dictionary[key] > 0 and dictionary[k - key] > 0:
                        answer += 1
                        dictionary[key] -= 1
                        dictionary[k - key] -= 1
                        
                    elif dictionary[key] > 0 and dictionary[k - key] == 0:
                        dictionary[key] = 0
                        
        return answer