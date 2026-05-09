# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, where sz is between 1 and 30,000, and n is a valid index for the list (1-indexed). The problem requires a solution with a time complexity of O(L), where L is the length of the linked list, and a space complexity of O(1), as only a constant amount of space can be used.

## Approach
We will use the two-pointer technique to solve this problem. The first pointer will move n steps ahead of the second pointer. Then, both pointers will move one step at a time until the first pointer reaches the end of the list. At this point, the second pointer will be at the node before the nth node from the end. We can then remove the nth node from the end.

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
- Use the two-pointer technique to solve linked list problems that involve removing nodes based on their position from the end.
- Always check for edge cases, such as when the node to be removed is the head of the list.
- Be careful when updating the next pointers of the nodes to avoid losing track of the nodes in the list.