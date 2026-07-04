# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, where sz is at least 1 and at most 30. You are given sz and the head of the linked list. The nodes are numbered from 0 to sz - 1. For example, if sz = 5 and the linked list is [1,2,3,4,5], then the nodes are numbered as follows: node 0 is 1, node 1 is 2, node 2 is 3, node 3 is 4, and node 4 is 5. If n = 2, then you should remove node 3 (which has value 4), resulting in the list [1,2,3,5]. The constraints are 1 <= sz <= 30, 1 <= n <= sz, and 0 <= Node.val <= 100.

## Approach
We use two pointers to traverse the linked list. The first pointer moves n steps ahead of the second pointer. When the first pointer reaches the end, the second pointer is at the nth node from the end.

## Complexity
- Time: O(L)
- Space: O(1)

## C++ Solution
```cpp
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // Create a dummy node
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        
        // Initialize two pointers
        ListNode* first = dummy;
        ListNode* second = dummy;
        
        // Move the first pointer n steps ahead
        for (int i = 0; i <= n; i++) {
            first = first->next;
        }
        
        // Move both pointers until the first pointer reaches the end
        while (first) {
            first = first->next;
            second = second->next;
        }
        
        // Remove the nth node from the end
        second->next = second->next->next;
        
        // Return the head of the modified list
        return dummy->next;
    }
};
```

## Test Cases
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Input: head = [1], n = 1
Output: []
Input: head = [1,2], n = 1
Output: [1]
```

## Key Takeaways
- Use two pointers to traverse the linked list and find the nth node from the end.
- Create a dummy node to simplify the removal of the head node.
- Move the first pointer n steps ahead and then move both pointers until the first pointer reaches the end.