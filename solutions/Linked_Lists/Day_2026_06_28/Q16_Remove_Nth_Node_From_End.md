# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, where sz is between 1 and 30,000. You are given the integer n which satisfies 1 <= n <= sz. The problem can be solved by using a two-pointer approach. For example, if we have a list 1 -> 2 -> 3 -> 4 -> 5 and we want to remove the 2nd node from the end, the resulting list should be 1 -> 2 -> 3 -> 5.

## Approach
The algorithm uses two pointers, both starting from the head of the list. The first pointer moves n steps ahead, then both pointers move one step at a time until the first pointer reaches the end of the list. At this point, the second pointer will be at the node right before the one we want to remove. We can then remove the nth node from the end by updating the next pointer of the second pointer's node.

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
        // Create two pointers
        ListNode* first = head;
        ListNode* second = head;
        
        // Move the first pointer n steps ahead
        for (int i = 0; i < n; i++) {
            first = first->next;
        }
        
        // If the first pointer is nullptr, it means we need to remove the head
        if (first == nullptr) {
            return head->next;
        }
        
        // Move both pointers one step at a time until the first pointer reaches the end
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
- Use a two-pointer approach to solve the problem efficiently.
- Handle the edge case where the node to be removed is the head of the list.
- Make sure to update the next pointer of the node before the one being removed to skip over it.