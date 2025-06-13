class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        max = sum(accounts[0])

        for i in range(1, len(accounts), 1):
            if sum(accounts[i]) > max: max = sum(accounts[i])

        return max