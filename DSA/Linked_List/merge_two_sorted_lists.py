"""
MERGE TWO SORTED LISTS
----------------------
Given the heads of two sorted linked lists, merge them into one
sorted linked list and return its head.

Example:
List1 : 1 -> 2 -> 4
List2 : 1 -> 3 -> 4

Output:
1 -> 1 -> 2 -> 3 -> 4 -> 4
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE (Copy, Sort, Rebuild)
# ─────────────────────────────────────────────
"""
Copy all values into an array, sort it, then build a new linked list.

Time  : O((n+m) log(n+m))
Space : O(n+m)
"""
def merge_two_lists_brute(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    values = []

    while list1 is not None:
        values.append(list1.val)
        list1 = list1.next

    while list2 is not None:
        values.append(list2.val)
        list2 = list2.next

    values.sort()

    dummy = ListNode()
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (Merge into Array)
# ─────────────────────────────────────────────
"""
Merge values into a sorted array, then build a new linked list.

Time  : O(n+m)
Space : O(n+m)
"""
def merge_two_lists_better(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    values = []

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            values.append(list1.val)
            list1 = list1.next
        else:
            values.append(list2.val)
            list2 = list2.next

    while list1 is not None:
        values.append(list1.val)
        list1 = list1.next

    while list2 is not None:
        values.append(list2.val)
        list2 = list2.next

    dummy = ListNode()
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Two Pointers)
# ─────────────────────────────────────────────
"""
Reuse the existing nodes.

Compare the current nodes of both lists.
Attach the smaller node and move its pointer.
Finally attach the remaining nodes.

Time  : O(n+m)
Space : O(1)
"""
def merge_two_lists_optimal(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    if list1 is not None:
        tail.next = list1
    else:
        tail.next = list2

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

    while head is not None:
        result.append(head.val)
        head = head.next

    return result


# ─────────────────────────────────────────────
if __name__ == "__main__":

    def test(fn):
        l1 = build_linked_list([1, 2, 4])
        l2 = build_linked_list([1, 3, 4])
        ans = fn(l1, l2)
        return linked_list_to_list(ans)

    print(test(merge_two_lists_brute))
    print(test(merge_two_lists_better))
    print(test(merge_two_lists_optimal))
