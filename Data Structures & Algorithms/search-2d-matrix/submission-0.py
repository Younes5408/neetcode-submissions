class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L,C=len(matrix),len(matrix[0])
        L1,L2 = 0 , L-1
        while L1<=L2:
            mid1=(L1+L2)//2
           
            if target > matrix[mid1][C-1]:
                L1=mid1+1
            elif target < matrix[mid1][0]:
                L2=mid1-1
            else :
                break
        le,r= 0 ,C -1
        row=(L1+L2)//2
        while le<=r:
            mid=(le+r)//2
            if target == matrix[row][mid]:
                return True 
            elif target > matrix[row][mid]:
                le=mid+1
            elif target <matrix[row][mid]:
                r=mid-1
        return False