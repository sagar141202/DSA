# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, where sz is between 1 and 30,000. You are given a non-empty linked list and a positive integer n, where n is less than or equal to sz. The problem can be solved by finding the (sz - n)th node from the beginning and removing the next node. For example, if we have a linked list 1 -> 2 -> 3 -> 4 -> 5 and n = 2, we should remove the 4th node from the beginning, resulting in 1 -> 2 -> 3 -> 5.

## Approach
The algorithm uses a two-pointer technique to traverse the linked list. We initialize two pointers, both pointing to the head of the list. We move the first pointer n steps ahead, then move both pointers one step at a time until the first pointer reaches the end of the list. At this point, the second pointer will be at the (sz - n)th node, and we can remove the next node.

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
        // Initialize two pointers, both pointing to the head of the list
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
        
        // Move both pointers one step at a time until the first pointer reaches the end of the list
        while (first->next != nullptr) {
            first = first->next;
            second = second->next;
        }
        
        // Remove the next node
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
- The two-pointer technique can be used to solve problems involving linked lists where we need to keep track of two nodes that are a certain distance apart.
- We should always handle edge cases, such as when the node to be removed is the head of the list.
- The time complexity of this solution is O(L), where L is the length of the linked list, because we only traverse the list once. The space complexity is O(1) because we only use a constant amount of space to store the two pointers.