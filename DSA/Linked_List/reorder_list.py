"""
REORDER LIST
------------
Given the head of a singly linked list L:

L0 → L1 → L2 → ... → Ln

Reorder it to:

L0 → Ln → L1 → Ln-1 → L2 → Ln-2 ...

You must reorder the list in-place.

Example:
Input :
1 -> 2 -> 3 -> 4 -> 5

Output:
1 -> 5 -> 2 -> 4 -> 3
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE (Using Array)
# ─────────────────────────────────────────────
"""
Store all nodes in an array.

Use two pointers from both ends and reconnect
the nodes in the required order.

Time  : O(n)
Space : O(n)
"""
def reorder_list_brute(head: Optional[ListNode]) -> None:
    if head is None:
        return

    nodes = []
    curr = head

    while curr is not None:
        nodes.append(curr)
        curr = curr.next

    left = 0
    right = len(nodes) - 1

    while left < right:
        nodes[left].next = nodes[right]
        left += 1

        if left == right:
            break

        nodes[right].next = nodes[left]
        right -= 1

    nodes[left].next = None


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Stack)
# ─────────────────────────────────────────────
"""
Push all nodes into a stack.

Traverse from the front while popping nodes
from the back to reorder the list.

Time  : O(n)
Space : O(n)
"""
def reorder_list_better(head: Optional[ListNode]) -> None:
    if head is None:
        return

    stack = []
    curr: Optional[ListNode] = head

    while curr is not None:
        stack.append(curr)
        curr = curr.next

    curr = head

    for _ in range(len(stack) // 2):
        last = stack.pop()
        assert curr is not None
        nxt = curr.next

        curr.next = last
        last.next = nxt

        curr = nxt

    assert curr is not None
    curr.next = None


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Find Middle + Reverse + Merge)
# ─────────────────────────────────────────────
"""
1. Find the middle of the list.
2. Reverse the second half.
3. Merge both halves alternately.

Time  : O(n)
Space : O(1)
"""
def reorder_list_optimal(head: Optional[ListNode]) -> None:
    if head is None or head.next is None:
        return

    # Find middle
    slow: ListNode = head
    fast: ListNode = head

    while fast.next is not None and fast.next.next is not None:
        assert slow.next is not None
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev: Optional[ListNode] = None
    curr: Optional[ListNode] = slow.next
    slow.next = None

    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # Merge two halves
    first: Optional[ListNode] = head
    second: Optional[ListNode] = prev

    while second is not None:
        assert first is not None
        tmp1 = first.next
        tmp2 = second.next

        first.next = second
        second.next = tmp1

        first = tmp1
        second = tmp2


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

    while head is not None:
        result.append(head.val)
        head = head.next

    return result


# ─────────────────────────────────────────────
if __name__ == "__main__":

    def test(fn):
        head = build_linked_list([1, 2, 3, 4, 5])
        fn(head)
        return linked_list_to_list(head)

    print(test(reorder_list_brute))
    print(test(reorder_list_better))
    print(test(reorder_list_optimal))