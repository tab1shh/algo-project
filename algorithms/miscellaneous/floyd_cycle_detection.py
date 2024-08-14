class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head):
    # Initialize two pointers, slow and fast, both starting at the head of the list
    slow = fast = head

    # Traverse the list until the fast pointer reaches the end or there is no next node
    while fast and fast.next:
        # Move slow pointer one step forward
        slow = slow.next
        # Move fast pointer two steps forward
        fast = fast.next.next

        # If slow and fast pointers meet, there is a cycle in the list
        if slow == fast:
            return True

    # If we exit the loop, it means fast pointer reached the end of the list, hence no cycle
    return False


def main():
    # Create nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    # Connect nodes to form a cycle
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Cycle here: node4 -> node2

    # Check if the list has a cycle
    result = has_cycle(node1)

    # Print the result
    print("List has a cycle:", result)


if __name__ == "__main__":
    main()
