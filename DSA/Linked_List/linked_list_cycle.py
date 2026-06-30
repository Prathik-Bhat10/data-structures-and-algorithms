"""
LINKED LIST CYCLE
-----------------
Given the head of a linked list, determine whether the linked
list has a cycle in it.

Return True if there is a cycle; otherwise False.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE (Visited List)
# ─────────────────────────────────────────────
"""
Store ids of visited nodes in a list.

Time  : O(n²)
Space : O(n)
"""
def has_cycle_brute(head: Optional[ListNode]) -> bool:
    visited = []
    curr = head

    while curr is not None:
        if id(curr) in visited:
            return True
        visited.append(id(curr))
        curr = curr.next

    return False


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Hash Set)
# ─────────────────────────────────────────────
"""
Store ids of visited nodes in a hash set.

Time  : O(n)
Space : O(n)
"""
def has_cycle_better(head: Optional[ListNode]) -> bool:
    visited = set()
    curr = head

    while curr is not None:
        if id(curr) in visited:
            return True
        visited.add(id(curr))
        curr = curr.next

    return False


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Floyd's Algorithm)
# ─────────────────────────────────────────────
"""
Two pointers:
slow -> one step
fast -> two steps

If they meet, a cycle exists.

Time  : O(n)
Space : O(1)
"""
def has_cycle_optimal(head: Optional[ListNode]) -> bool:
    if head is None:
        return False

    slow: Optional[ListNode] = head
    fast: Optional[ListNode] = head

    while fast is not None and fast.next is not None:
        # At this point slow cannot be None because
        # if fast can move two steps, slow can move one.
        assert slow is not None

        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


# ─────────────────────────────────────────────
# Helper Functions
# ─────────────────────────────────────────────
def build_linked_list(values):
    dummy = ListNode()
    curr = dummy

    for value in values:
        curr.next = ListNode(value)
        curr = curr.next

    return dummy.next


def make_cycle(head: Optional[ListNode], pos: int) -> Optional[ListNode]:
    if head is None or pos == -1:
        return head

    cycle_node = None
    tail = head
    index = 0

    while tail is not None:
        if index == pos:
            cycle_node = tail

        if tail.next is None:
            break

        tail = tail.next
        index += 1

    if cycle_node is not None and tail is not None:
        tail.next = cycle_node

    return head


# ─────────────────────────────────────────────
if __name__ == "__main__":
    head = build_linked_list([3, 2, 0, -4])
    make_cycle(head, 1)

    print(has_cycle_brute(head))
    print(has_cycle_better(head))
    print(has_cycle_optimal(head))

    head2 = build_linked_list([1, 2, 3, 4])

    print(has_cycle_brute(head2))
    print(has_cycle_better(head2))
    print(has_cycle_optimal(head2))
