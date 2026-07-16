# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, where sz is between 1 and 30. For example, with n = 1, the last node will be removed, with n = 2, the second last node will be removed, and so on. It is guaranteed that n is a valid node to remove, i.e., 1 ≤ n ≤ sz.

## Approach
We can solve this problem using a two-pointer technique, where the first pointer is nth nodes ahead of the second pointer. When the first pointer reaches the end of the list, the second pointer will be at the node right before the one we want to remove. We then skip the node to be removed by updating the next pointer of the second pointer.

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
        
        // If the first pointer has reached the end, remove the head node
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
- Use two pointers to track the node to be removed and the node before it.
- Move the first pointer nth nodes ahead to create a gap between the two pointers.
- Remove the node by updating the next pointer of the second pointer.