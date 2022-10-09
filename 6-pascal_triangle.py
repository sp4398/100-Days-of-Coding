class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        mat=[]
        mat.append([1])
        for i in range(numRows-1):
            new=[1]
            for j in range(0,i):
                new.append(mat[i][j]+mat[i][j+1])
            new.append(1)
            mat.append(new)
        return mat
