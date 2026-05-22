# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, and 1 ≤ n ≤ sz. The nodes in the list are numbered from 1 to sz. You are given the head of the linked list and the integer n, and you need to find the node that is nth from the end and remove it. For example, if we have a list 1 -> 2 -> 3 -> 4 -> 5 and n = 2, then the node with value 4 should be removed, resulting in the list 1 -> 2 -> 3 -> 5.

## Approach
We can solve this problem by using two pointers that are n nodes apart. We move both pointers one step at a time until the first pointer reaches the end of the list. At this point, the second pointer will be at the nth node from the end. We can then remove this node from the list.

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
        // Initialize two pointers, p1 and p2, to the head of the list
        ListNode* p1 = head;
        ListNode* p2 = head;
        
        // Move p1 n nodes ahead
        for (int i = 0; i < n; i++) {
            p1 = p1->next;
        }
        
        // If p1 is nullptr, it means we need to remove the head
        if (p1 == nullptr) {
            return head->next;
        }
        
        // Move both pointers one step at a time until p1 reaches the end
        while (p1->next != nullptr) {
            p1 = p1->next;
            p2 = p2->next;
        }
        
        // Remove the nth node from the end
        p2->next = p2->next->next;
        
        return head;
    }
};
```

## Test Cases
```
Input: head = [1, 2, 3, 4, 5], n = 2
Output: [1, 2, 3, 5]
Input: head = [1], n = 1
Output: []
Input: head = [1, 2], n = 1
Output: [1]
```

## Key Takeaways
- We use two pointers to solve this problem efficiently.
- The time complexity is O(L), where L is the length of the linked list, because we make one pass through the list.
- The space complexity is O(1) because we use a constant amount of space to store the pointers and other variables.