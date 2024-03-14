class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atMost(nums, goal) - self.atMost(nums, goal - 1)
        
    def atMost(self, nums: List[int], goal: int) -> int:
        
        head = tail = current_sum = answer = 0
        
        for head in range(0, len(nums), 1):
            current_sum += nums[head]
            while current_sum > goal and tail <= head:
                current_sum -= nums[tail]
                tail += 1
            answer += head - tail + 1
        
        return answer
            