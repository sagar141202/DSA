# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, where sz is between 1 and 30,000. You are given sz and the head of the linked list. The nodes are numbered from 1 to sz. You must remove the nth node from the end, which means if sz = 5 and n = 2, you need to remove the 4th node from the beginning (1-indexed), as it's the 2nd node from the end. The solution should handle cases where n is equal to sz.

## Approach
To solve this problem, we will use two pointers, both starting at the head of the list. The first pointer will move n steps ahead, and then both pointers will move one step at a time until the first pointer reaches the end of the list. At this point, the second pointer will be at the node right before the one we need to remove. We will then remove the nth node from the end by updating the next pointer of the second pointer's node.

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
        // Initialize two pointers, p1 and p2, both at the head of the list
        ListNode* p1 = head;
        ListNode* p2 = head;
        
        // Move p1 n steps ahead
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
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Input: head = [1], n = 1
Output: []
Input: head = [1,2], n = 1
Output: [1]
```

## Key Takeaways
- Use two pointers to solve this problem efficiently, avoiding the need to know the length of the list beforehand.
- The first pointer moves n steps ahead, and then both pointers move one step at a time until the first pointer reaches the end of the list.
- By the time the first pointer reaches the end, the second pointer will be at the node right before the one that needs to be removed.