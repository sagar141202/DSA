# Remove Nth Node From End

## Problem Statement
Given the head of a linked list, remove the nth node from the end of the list and return its head. The number of nodes in the list is sz, where sz is at least n. You are given the head of the list and the integer n. For example, if we have a list 1 -> 2 -> 3 -> 4 -> 5 and n = 2, then the output should be 1 -> 2 -> 3 -> 5.

## Approach
We use two pointers that are n nodes apart to traverse the linked list. When the leading pointer reaches the end of the list, the trailing pointer will be at the nth node from the end. We then remove this node from the list.

## Complexity
- Time: O(L)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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
        // Initialize two pointers
        ListNode* first = head;
        ListNode* second = head;
        
        // Move the first pointer n nodes ahead
        for (int i = 0; i < n; i++) {
            first = first->next;
        }
        
        // If first pointer has reached the end, remove the head
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
- Use two pointers to solve linked list problems that require tracking nodes at a certain distance apart.
- Be careful when removing nodes from a linked list, as it requires updating the next pointers of adjacent nodes.
- Consider edge cases, such as when the node to be removed is the head of the list.