class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        
        hashMap = {key:_ for _, key in enumerate(friends)}
        output = []

        for participant in order:
            if hashMap.get(participant) != None: output.append(participant)

        return output