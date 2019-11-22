# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        l, p = [self.val], self.next
        while (p != None):
            l.append(p.val)
            p = p.next
        return str(l)


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p1, p2 = dummy, dummy
        for i in range(n):
            p1 = p1.next
        while p1.next != None:
            p1, p2 = p1.next, p2.next
        p2.next = p2.next.next
        return dummy.next


if __name__ == "__main__":
    def buildListNode(l):
        head = ListNode(l[0])
        cur = head
        for i in range(1, len(l)):
            cur.next = ListNode(l[i])
            cur = cur.next
        return head

    s = Solution()
    print(s.removeNthFromEnd(buildListNode([1, 2, 3, 4, 5]), 2))
    print(s.removeNthFromEnd(buildListNode([1, 2, 3, 4, 5]), 1))
    print(s.removeNthFromEnd(buildListNode([1]), 1))
