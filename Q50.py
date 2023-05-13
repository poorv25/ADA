class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def merge_sort(head):
    if not head or not head.next:
        return head
    
    # Divide the linked list into two halves
    mid = get_mid(head)
    left_head = head
    right_head = mid.next
    mid.next = None
    
    # Recursively sort the two halves
    left_sorted = merge_sort(left_head)
    right_sorted = merge_sort(right_head)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def get_mid(head):
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    dummy = Node(0)
    cur = dummy
    while left and right:
        if left.val < right.val:
            cur.next = left
            left = left.next
        else:
            cur.next = right
            right = right.next
        cur = cur.next
    cur.next = left or right
    return dummy.next
