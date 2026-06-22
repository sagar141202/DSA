# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The linked list has a maximum of 5000 nodes, and each node has a value ranging from 0 to 5000. For example, if we have a linked list 1 -> 2 -> 3 -> 4 -> 5, the reversed linked list should be 5 -> 4 -> 3 -> 2 -> 1.

## Approach
We can solve this problem by initializing three pointers: previous, current, and next. We will traverse the linked list, and for each node, we will reverse the next pointer to point to the previous node. This approach will reverse the linked list in-place.

## Complexity
- Time: O(n)
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
    ListNode* reverseList(ListNode* head) {
        // Initialize three pointers: previous, current, and next
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (curr) {
            // Store the next node in the next pointer
            ListNode* nextTemp = curr->next;
            // Reverse the next pointer to point to the previous node
            curr->next = prev;
            // Move the previous and current pointers one step forward
            prev = curr;
            curr = nextTemp;
        }
        // At the end of the loop, the previous pointer will point to the new head
        return prev;
    }
};
```

## Test Cases
```
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
Input: [1, 2]
Output: [2, 1]
Input: []
Output: []
```

## Key Takeaways
- We use three pointers (previous, current, and next) to reverse the linked list in-place.
- We traverse the linked list only once, resulting in a time complexity of O(n).
- We do not use any extra space that scales with the input size, resulting in a space complexity of O(1).