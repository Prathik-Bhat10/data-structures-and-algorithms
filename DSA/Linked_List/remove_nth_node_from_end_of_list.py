"""
REMOVE NTH NODE FROM END OF LIST
--------------------------------
Given the head of a linked list, remove the nth node from the end
of the list and return its head.

Example:
Input :
head = [1,2,3,4,5]
n = 2

Output:
[1,2,3,5]

Explanation:

Original:
1 → 2 → 3 → 4 → 5

Remove the 2nd node from the end (4):

Result:
1 → 2 → 3 → 5
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE (Length of List)
# ─────────────────────────────────────────────
"""
Idea:
1. Find the total length of the list.
2. Compute the position of the node to remove from the front.
3. Traverse again and remove it.

Example:

1 → 2 → 3 → 4 → 5
Length = 5

n = 2

Node to remove from front:
5 - 2 = 3

Delete node after index 2.

Time  : O(n)
Space : O(1)
"""

def remove_nth_from_end_brute(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head

    length = 0
    curr: Optional[ListNode] = head

    while curr is not None:
        length += 1
        curr = curr.next

    curr = dummy

    for _ in range(length - n):
        assert curr is not None
        curr = curr.next

    assert curr is not None
    if curr.next is not None:
        curr.next = curr.next.next

    return dummy.next


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Stack)
# ─────────────────────────────────────────────
"""
Idea:
Store every node in a stack.

Since stacks are LIFO,
the nth node popped corresponds to the nth node from the end.

Example:

1 → 2 → 3 → 4 → 5

Stack:
[1,2,3,4,5]

Pop:
5
4  ← remove this node

Time  : O(n)
Space : O(n)
"""

def remove_nth_from_end_stack(head, n):
    dummy = ListNode(0)
    dummy.next = head

    stack = []

    curr = dummy

    while curr is not None:
        stack.append(curr)
        curr = curr.next

    for _ in range(n):
        stack.pop()

    prev = stack[-1]
    prev.next = prev.next.next

    return dummy.next


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Two Pointers)
# ─────────────────────────────────────────────
"""
Observation:
Maintain a gap of n nodes between two pointers.

Steps:
1. Create a dummy node.
2. Move fast pointer n+1 steps.
3. Move both pointers together.
4. When fast reaches the end,
   slow will be just before the node to delete.

Example:

head = 1 → 2 → 3 → 4 → 5
n = 2

Initially:

D → 1 → 2 → 3 → 4 → 5
S
F

Move Fast 3 steps:

D → 1 → 2 → 3 → 4 → 5
S           F

Move together:

D → 1 → 2 → 3 → 4 → 5
          S           F

Slow stops before node 4.

Delete:

slow.next = slow.next.next

Result:

1 → 2 → 3 → 5

Time  : O(n)
Space : O(1)

This is the expected interview / LeetCode solution.
"""

def remove_nth_from_end_optimal(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head

    slow: Optional[ListNode] = dummy
    fast: Optional[ListNode] = dummy

    for _ in range(n + 1):
        if fast is not None:
            fast = fast.next
        else:
            break

    while fast is not None:
        assert slow is not None
        slow = slow.next
        fast = fast.next

    assert slow is not None
    if slow.next is not None:
        slow.next = slow.next.next

    return dummy.next


# ─────────────────────────────────────────────
# Helper Functions
# ─────────────────────────────────────────────

def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy

    for val in values:
        curr.next = ListNode(val)
        curr = curr.next

    return dummy.next


def print_linked_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    print(result)


# ─────────────────────────────────────────────
if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4, 5])
    n = 2

    print_linked_list(remove_nth_from_end_brute(build_linked_list([1,2,3,4,5]), n))
    print_linked_list(remove_nth_from_end_stack(build_linked_list([1,2,3,4,5]), n))
    print_linked_list(remove_nth_from_end_optimal(build_linked_list([1,2,3,4,5]), n))