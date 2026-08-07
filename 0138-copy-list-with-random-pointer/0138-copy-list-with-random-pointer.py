# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        l1 = head
        mapp = {None:None}
        while l1:
            mapp[l1] = Node(l1.val)
            l1 = l1.next
        l1 = head
        while l1:
            mapp[l1].next = mapp[l1.next]
            mapp[l1].random = mapp[l1.random]
            l1 = l1.next
        return mapp[head]