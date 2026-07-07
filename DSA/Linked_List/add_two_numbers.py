"""
ADD TWO NUMBERS
---------------
You are given two non-empty linked lists representing two
non-negative integers.

The digits are stored in reverse order, and each node contains
a single digit.

Add the two numbers and return the sum as a linked list.

Example:
List1 : 2 -> 4 -> 3
List2 : 5 -> 6 -> 4

Output:
7 -> 0 -> 8

Explanation:
342 + 465 = 807
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE (Convert to Integer)
# ─────────────────────────────────────────────
"""
Convert both linked lists into integers.
Add them.
Create a new linked list from the resulting number.

Time  : O(n+m)
Space : O(max(n,m))
"""
def add_two_numbers_brute(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:

    num1 = 0
    num2 = 0
    place = 1

    curr = l1
    while curr:
        num1 += curr.val * place
        place *= 10
        curr = curr.next

    place = 1
    curr = l2
    while curr:
        num2 += curr.val * place
        place *= 10
        curr = curr.next

    total = num1 + num2

    if total == 0:
        return ListNode(0)

    dummy = ListNode()
    tail = dummy

    while total > 0:
        tail.next = ListNode(total % 10)
        tail = tail.next
        total //= 10

    return dummy.next


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Store Digits First)
# ─────────────────────────────────────────────
"""
Store digits in an array while performing addition.
Build the linked list afterward.

Time  : O(max(n,m))
Space : O(max(n,m))
"""
def add_two_numbers_better(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:

    digits = []
    carry = 0

    while l1 or l2 or carry:

        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        total = x + y + carry
        digits.append(total % 10)
        carry = total // 10

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    dummy = ListNode()
    tail = dummy

    for digit in digits:
        tail.next = ListNode(digit)
        tail = tail.next

    return dummy.next


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Single Traversal)
# ─────────────────────────────────────────────
"""
Traverse both linked lists simultaneously.

At each step:
- Add corresponding digits.
- Include carry from previous addition.
- Create a new node with current digit.
- Update carry.

Time  : O(max(n,m))
Space : O(max(n,m))   (output list excluded in interview discussions)
"""
def add_two_numbers_optimal(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:

    dummy = ListNode()
    tail = dummy
    carry = 0

    while l1 or l2 or carry:

        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        total = x + y + carry
        carry = total // 10

        tail.next = ListNode(total % 10)
        tail = tail.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next


# ─────────────────────────────────────────────
# Helper Functions
# ─────────────────────────────────────────────
def build_linked_list(values):
    dummy = ListNode()
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


# ─────────────────────────────────────────────
if __name__ == "__main__":

    def test(fn):
        l1 = build_linked_list([2, 4, 3])
        l2 = build_linked_list([5, 6, 4])
        ans = fn(l1, l2)
        return linked_list_to_list(ans)

    print(test(add_two_numbers_brute))
    print(test(add_two_numbers_better))
    print(test(add_two_numbers_optimal))