"""
REVERSE A LINKED LIST
---------------------
Given the head of a singly linked list, reverse the list and
return the new head.

Example:
Input : 1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1

Example:
Input : 1 -> 2
Output: 2 -> 1

Example:
Input : []
Output: []
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE (Using Extra Array)
# ─────────────────────────────────────────────
"""
Store all node values in an array, then traverse the linked list
again and overwrite each node with values in reverse order.

The structure of the linked list does not change—only the values
inside the nodes are updated.

Example:
1 -> 2 -> 3 -> 4

Values stored:
[1, 2, 3, 4]

Overwrite:
4 -> 3 -> 2 -> 1

Time  : O(n)
Space : O(n)
"""


def reverse_list_brute(head: Optional[ListNode]) -> Optional[ListNode]:
    values = []

    curr = head
    while curr:
        values.append(curr.val)
        curr = curr.next

    curr = head
    while curr:
        curr.val = values.pop()
        curr = curr.next

    return head


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Using Stack)
# ─────────────────────────────────────────────
"""
Push every node onto a stack.

The last node becomes the new head.
Pop nodes one by one and reconnect them.

Example:

1 -> 2 -> 3 -> 4

Stack:
[top]
4
3
2
1

Pop:
head = 4
4 -> 3 -> 2 -> 1

Extra space is required for the stack.

Time  : O(n)
Space : O(n)
"""


def reverse_list_stack(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head

    stack = []

    curr = head
    while curr:
        stack.append(curr)
        curr = curr.next

    new_head = stack.pop()
    curr = new_head

    while stack:
        curr.next = stack.pop()
        curr = curr.next

    curr.next = None

    return new_head


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Three Pointer Technique)
# ─────────────────────────────────────────────
"""
Maintain three pointers:

prev -> already reversed part
curr -> current node
next -> saves next node before changing links

Initially:

None <- 1 -> 2 -> 3 -> 4

Step 1:
prev = None
curr = 1
next = 2

Reverse:
1 -> None

Move pointers

None <- 1     2 -> 3 -> 4
       ↑
     prev

Step 2:

None <- 1 <- 2     3 -> 4

Step 3:

None <- 1 <- 2 <- 3     4

Step 4:

None <- 1 <- 2 <- 3 <- 4

curr becomes None.

prev points to the new head.

Time  : O(n)
Space : O(1)
"""


def reverse_list_optimal(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev

        prev = curr
        curr = nxt

    return prev


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


def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


# ─────────────────────────────────────────────
if __name__ == "__main__":

    def test(fn, values):
        head = build_linked_list(values)
        new_head = fn(head)
        return linked_list_to_list(new_head)

    print(test(reverse_list_brute, [1, 2, 3, 4, 5]))
    # [5, 4, 3, 2, 1]

    print(test(reverse_list_stack, [1, 2, 3, 4, 5]))
    # [5, 4, 3, 2, 1]

    print(test(reverse_list_optimal, [1, 2, 3, 4, 5]))
    # [5, 4, 3, 2, 1]