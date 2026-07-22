# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, where sz is between 1 and 30,000. n will always be valid and 1-based, meaning the last node is the first node with 1 node in the list. For example, if we have a list 1 -> 2 -> 3 -> 4 -> 5 and n = 2, then the node with value 4 should be removed, resulting in the list 1 -> 2 -> 3 -> 5.

## Approach
We can solve this problem by using two pointers that are n nodes apart. When the first pointer reaches the end of the list, the second pointer will be at the node right before the one we want to remove. We can then remove the nth node from the end by updating the next pointer of the second pointer's node.

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
        
        // Move both pointers one node at a time until p1 reaches the end
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
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Input: head = [1], n = 1
Output: []
Input: head = [1,2], n = 1
Output: [1]
```

## Key Takeaways
- Use two pointers to solve linked list problems that involve removing nodes based on their position from the end.
- Always check for edge cases, such as when the node to be removed is the head of the list.
- Be careful when updating pointers to avoid losing track of nodes in the list.