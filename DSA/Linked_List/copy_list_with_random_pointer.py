"""
COPY LIST WITH RANDOM POINTER
-----------------------------
A linked list is given where each node contains:
1. next pointer
2. random pointer (can point to any node or None)

Create a deep copy of the linked list.

Example:

Original:
7 -> 13 -> 11 -> 10 -> 1

Random:
7.random   = None
13.random  = 7
11.random  = 1
10.random  = 11
1.random   = 7

Output:
A completely new linked list having the same values,
next pointers, and random pointers.
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next: Optional["Node"] = None, random: Optional["Node"] = None):
        self.val = x
        self.next = next
        self.random = random


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE (Recursive Copy)
# ─────────────────────────────────────────────
"""
Recursively create every node.

Use a hashmap to avoid creating duplicate nodes and
to correctly connect random pointers.

Time  : O(n)
Space : O(n)
"""
def copy_random_list_brute(head: Optional[Node]) -> Optional[Node]:
    visited = {}

    def dfs(node):
        if node is None:
            return None

        if node in visited:
            return visited[node]

        copy = Node(node.val)
        visited[node] = copy

        copy.next = dfs(node.next)
        copy.random = dfs(node.random)

        return copy

    return dfs(head)


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (HashMap)
# ─────────────────────────────────────────────
"""
Create copies of every node and store the mapping.

Second pass:
Connect next and random pointers using the hashmap.

Time  : O(n)
Space : O(n)
"""
def copy_random_list_better(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        return None

    mapping = {}

    curr = head

    while curr is not None:
        mapping[curr] = Node(curr.val)
        curr = curr.next

    curr = head

    while curr is not None:
        mapping[curr].next = mapping.get(curr.next)
        mapping[curr].random = mapping.get(curr.random)
        curr = curr.next

    return mapping[head]


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (Interleaving Nodes)
# ─────────────────────────────────────────────
"""
Step 1:
Insert copied nodes between original nodes.

A -> B -> C
becomes

A -> A' -> B -> B' -> C -> C'

Step 2:
Assign random pointers.

copy.random = original.random.next

Step 3:
Separate the copied list from the original list.

Time  : O(n)
Space : O(1)
"""
def copy_random_list_optimal(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        return None

    # Insert copied nodes
    curr: Optional[Node] = head

    while curr is not None:
        copy = Node(curr.val)
        copy.next = curr.next
        curr.next = copy
        curr = copy.next

    # Assign random pointers
    curr = head

    while curr is not None:
        if curr.random is not None:
            assert curr.next is not None
            curr.next.random = curr.random.next
        curr = curr.next.next if curr.next is not None else None

    # Separate both lists
    dummy = Node(0)
    copy_curr = dummy
    curr = head

    while curr is not None:
        copy = curr.next
        assert copy is not None

        curr.next = copy.next
        copy_curr.next = copy

        copy_curr = copy_curr.next
        curr = curr.next

    return dummy.next


# ─────────────────────────────────────────────
# Helper Functions
# ─────────────────────────────────────────────
def build_sample_list():
    """
    Creates:

    7 -> 13 -> 11 -> 10 -> 1

    Random:
    None, 7, 1, 11, 7
    """

    nodes = [Node(7), Node(13), Node(11), Node(10), Node(1)]

    for i in range(4):
        nodes[i].next = nodes[i + 1]

    nodes[1].random = nodes[0]
    nodes[2].random = nodes[4]
    nodes[3].random = nodes[2]
    nodes[4].random = nodes[0]

    return nodes[0]


def print_list(head):
    curr = head

    while curr is not None:
        random_val = curr.random.val if curr.random else None
        print(f"Node({curr.val}) -> Random({random_val})")
        curr = curr.next


# ─────────────────────────────────────────────
if __name__ == "__main__":

    def test(fn):
        head = build_sample_list()
        copied = fn(head)
        print_list(copied)
        print("-" * 30)

    test(copy_random_list_brute)
    test(copy_random_list_better)
    test(copy_random_list_optimal)