class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_v = 0
        l_h = 0 
        m_v = len(matrix) - 1
        m_h = len(matrix[0]) - 1
        r = 0
        
        while l_v <= m_v:
            mid = (m_v + l_v) // 2
            if target > matrix[mid][-1]:
                l_v = mid + 1
            elif target < matrix[mid][0]:
                m_v = mid - 1
            else:
                r = mid
                break
        else:
            return False

        while l_h <= m_h:
            mid = (l_h + m_h) // 2
            if target > matrix[r][mid]:
                l_h = mid + 1
            elif target < matrix[r][mid]:
                m_h = mid - 1
            else:
                return True

        return False