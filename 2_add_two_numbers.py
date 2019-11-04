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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        incr, head = 0, ListNode(0)
        dummy = head
        while (l1 != None or l2 != None):
            incr, sum = 0, (l1.val if l1 != None else 0) + (l2.val if l2 != None else 0) + incr
            if sum >= 10:
                incr, sum = 1, sum - 10
            head.next = ListNode(sum)
            l1, l2, head = l1.next if l1 != None else None, l2.next if l2 != None else None, head.next
        if incr != 0:
            head.next = ListNode(incr)
        return dummy.next


if __name__ == "__main__":
    l1_0, l1_1, l1_2 = ListNode(2), ListNode(4), ListNode(3)
    l1_0.next, l1_1.next = l1_1, l1_2
    l2_0, l2_1, l2_2 = ListNode(5), ListNode(6), ListNode(4)
    l2_0.next, l2_1.next = l2_1, l2_2
    print(Solution().addTwoNumbers(l1_0, l2_0))
    print(Solution().addTwoNumbers(ListNode(5), ListNode(5)))
