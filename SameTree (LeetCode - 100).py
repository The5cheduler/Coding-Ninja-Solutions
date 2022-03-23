class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#DFS Way
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p,q)]
        while stack:
            p,q = stack.pop()
            if not p and not q:
                continue
            if (not p or not q) or (p.val != q.val):
                return False
            stack.extend([(p.left,q.left),(p.right,q.right)])
        return True
