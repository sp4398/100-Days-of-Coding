class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operation = []
        targetIndex=0

        for i in range(1,n+1):
            if targetIndex==len(target):
                break
            
            if target[targetIndex]==i:
                operation.append("Push")
                targetIndex+=1

            else:
                operation.append("Push")
                operation.append("Pop")

        return operation
        
