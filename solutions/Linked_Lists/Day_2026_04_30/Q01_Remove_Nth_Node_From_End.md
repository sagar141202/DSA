# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, and 1 <= n <= sz. You are required to solve this problem in one pass, i.e., you cannot traverse the linked list twice. For example, given the linked list 1 -> 2 -> 3 -> 4 -> 5 and n = 2, the output should be 1 -> 2 -> 3 -> 5.

## Approach
We can use two pointers to solve this problem. The first pointer will be nth nodes ahead of the second pointer. When the first pointer reaches the end, the second pointer will be at the node before the node to be removed. We can then remove the nth node from the end.

## Complexity
- Time: O(L)
- Space: O(1)

## C++ Solution
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // Initialize two pointers
        ListNode* first = head;
        ListNode* second = head;
        
        // Move the first pointer nth nodes ahead
        for (int i = 0; i < n; i++) {
            first = first->next;
        }
        
        // If the first pointer has reached the end, it means the head is the node to be removed
        if (first == nullptr) {
            return head->next;
        }
        
        // Move both pointers until the first pointer reaches the end
        while (first->next != nullptr) {
            first = first->next;
            second = second->next;
        }
        
        // Remove the nth node from the end
        second->next = second->next->next;
        
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
- We can use two pointers to solve this problem in one pass.
- The first pointer should be nth nodes ahead of the second pointer.
- When the first pointer reaches the end, the second pointer will be at the node before the node to be removed.