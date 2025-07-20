class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        start_bin_str = str(bin(start))[2:]
        goal_bin_str = str(bin(goal))[2:]
        output = 0

        max_len = max(len(start_bin_str), len(goal_bin_str))
        start_bin_str = start_bin_str.rjust(max_len, '0')
        goal_bin_str = goal_bin_str.rjust(max_len, '0')

        for i in range(0, len(start_bin_str), 1):
            if start_bin_str[i] != goal_bin_str[i]: output += 1

        return output