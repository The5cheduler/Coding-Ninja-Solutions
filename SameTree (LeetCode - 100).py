import queue
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#DFS Way (Run Time - O(n), Space Time - Constant O(1))
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

#BFS way (Run Time - O(n), Space Time - Constant O(1))
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queue = queue.dequeue([p, q])
        while queue:
            p,q = queue.popleft()
            if not p and not q:
                continue
            if (not p or not q) or (p.val != q.val):
                return False
            queue.extend([(p.left,q.left),(p.right,q.right)])
        return True

