# https://leetcode.com/problems/search-a-2d-matrix/submissions/1220141376/

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def searchArray(array: list, target: int) -> bool:
            min_pos, max_pos = 0, len(array)

            while min_pos < max_pos:
                midpoint = int(max_pos - (max_pos - min_pos) / 2)

                if array[midpoint] > target:
                    max_pos = midpoint
                elif array[midpoint] < target:
                    min_pos = midpoint + 1
                else:
                    return True
            
            return False
        
        for index, array in enumerate(matrix):
            if array[-1] > target:
                return searchArray(matrix[index], target)
            elif array[-1] == target:
                return True
        
        return False