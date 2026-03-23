# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, where sz is in the range [1, 10^5]. The value of each node is in the range [-10^5, 10^5]. The value of n is valid, i.e., 1 <= n <= sz. For example, if the list is 1 -> 2 -> 3 -> 4 -> 5 and n = 2, the output should be 1 -> 2 -> 3 -> 5.

## Approach
We can solve this problem by using two pointers, one at the head and the other at the nth node from the head. Then we move both pointers one step at a time until the second pointer reaches the end. The first pointer will be at the (sz - n)th node, which is the node before the one we want to remove. We can then remove the nth node from the end by changing the next pointer of the first pointer.

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
        // Create two pointers, both at the head
        ListNode* first = head;
        ListNode* second = head;
        
        // Move the second pointer n steps ahead
        for (int i = 0; i < n; i++) {
            second = second->next;
        }
        
        // If the second pointer is nullptr, it means we need to remove the head
        if (second == nullptr) {
            return head->next;
        }
        
        // Move both pointers one step at a time until the second pointer reaches the end
        while (second->next != nullptr) {
            first = first->next;
            second = second->next;
        }
        
        // Remove the nth node from the end
        first->next = first->next->next;
        
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
- Use two pointers to solve this problem efficiently.
- Move the second pointer n steps ahead of the first pointer.
- Remove the nth node from the end by changing the next pointer of the first pointer.