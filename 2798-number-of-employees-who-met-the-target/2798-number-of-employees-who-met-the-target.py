class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        
        count = 0

        for time_worked in hours:
            if time_worked >= target:
                count += 1

        return count