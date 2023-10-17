class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indeg=[0]*n
        for i in range(n):
            if leftChild[i]!=-1:
                indeg[leftChild[i]]+=1
            if rightChild[i]!=-1:
                indeg[rightChild[i]]+=1

        root=None
        for i in range(n):
            if indeg[i]==0:
                if root is None:
                    root=i
                else:
                    return False

        if root is None:
            return False

        visited=[False]*n
        queue=deque([root])
        while queue:
            node=queue.popleft()
            if visited[node]:
                return False
            visited[node]=True
            if leftChild[node]!=-1:
                queue.append(leftChild[node])
            if rightChild[node]!= -1:
                queue.append(rightChild[node])

        return sum(visited)==n
