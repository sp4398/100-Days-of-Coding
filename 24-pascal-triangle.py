class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp=[[1],[]]

        for i in range(1,rowIndex+1):
            dp[1].append(1)

            cur=dp[1]
            prev=dp[0]

            for j in range(1,len(prev)):
                sum=prev[j]+prev[j-1]
                cur.append(sum)

            cur.append(1)
            dp[0]=dp[1][:]
            dp[1]=[]

        return dp[0]
