# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, and 1 ≤ n ≤ sz. The solution should only use constant extra memory and make one pass through the list. For example, if we have a list 1 -> 2 -> 3 -> 4 -> 5 and n = 2, the output should be 1 -> 2 -> 3 -> 5.

## Approach
We can solve this problem by using two pointers, p1 and p2, where p2 is n steps ahead of p1. When p2 reaches the end of the list, p1 will be at the node before the nth node from the end. We can then remove the nth node by updating the next pointer of p1.

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
        // Initialize two pointers, p1 and p2
        ListNode* p1 = head;
        ListNode* p2 = head;
        
        // Move p2 n steps ahead
        for (int i = 0; i < n; i++) {
            p2 = p2->next;
        }
        
        // If p2 is nullptr, it means we need to remove the head
        if (p2 == nullptr) {
            return head->next;
        }
        
        // Move both pointers until p2 reaches the end
        while (p2->next != nullptr) {
            p1 = p1->next;
            p2 = p2->next;
        }
        
        // Remove the nth node from the end
        p1->next = p1->next->next;
        
        return head;
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
- We can use two pointers to solve this problem in one pass with constant extra memory.
- The key is to move the second pointer n steps ahead and then move both pointers together until the second pointer reaches the end.
- We need to handle the edge case where the node to be removed is the head of the list.