class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]

        list_for_current_row = list_for_previous_row = [1, 1]
        current_row_index = 2

        while True:

            for index in range(0, len(list_for_previous_row) - 1, 1):
                penult = len(list_for_current_row) - 1
                list_for_current_row.insert(penult, list_for_previous_row[index] + list_for_previous_row[index + 1])

            if current_row_index == rowIndex:
                return list_for_current_row

            list_for_previous_row = list_for_current_row # Track the previous row
            current_row_index += 1
            list_for_current_row = [1, 1] # Reset list for the current row