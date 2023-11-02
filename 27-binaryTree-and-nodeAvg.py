class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res=0

        def traverse(node):
            nonlocal res

            if not node:
                return 0, 0
            left_sum,left_count=traverse(node.left)
            right_sum,right_count=traverse(node.right)

            cur_sum=node.val+left_sum+right_sum
            cur_count=1+left_count+right_count

            if cur_sum//cur_count==node.val:
                res+=1

            return cur_sum,cur_count
        traverse(root)
        return res
