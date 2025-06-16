class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        ops = {"--X": -1, "X--": -1, "X++": 1, "++X": 1}
        output = 0

        for op in operations:
            output += ops[op]

        return output