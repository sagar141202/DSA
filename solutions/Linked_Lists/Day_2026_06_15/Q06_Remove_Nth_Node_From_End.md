# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, and sz is within the range [1, 30]. For example, if we have a list 1 -> 2 -> 3 -> 4 -> 5 and n = 2, then after removing the 2nd node from the end, the list becomes 1 -> 2 -> 3 -> 5. 

## Approach
We can use two pointers to solve this problem, where the first pointer is n steps ahead of the second pointer. When the first pointer reaches the end, the second pointer will be at the node before the nth node from the end. We can then remove the nth node from the end by updating the next pointer of the second pointer.

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
        // Create two pointers, p1 and p2, both pointing at the head
        ListNode* p1 = head;
        ListNode* p2 = head;
        
        // Move p1 n steps forward
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
- Use two pointers to solve this problem, where the first pointer is n steps ahead of the second pointer.
- When the first pointer reaches the end, the second pointer will be at the node before the nth node from the end.
- We can remove the nth node from the end by updating the next pointer of the second pointer.