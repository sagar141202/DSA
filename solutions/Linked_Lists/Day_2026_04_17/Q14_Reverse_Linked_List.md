# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes' values are in the range [-5000, 5000]. The list is guaranteed to be non-empty, except for the case where the list is empty. For example, if the input is [1,2,3,4,5], the output should be [5,4,3,2,1].

## Approach
The algorithm to reverse a linked list involves initializing three pointers: previous, current, and next. We initialize the previous pointer to NULL and the current pointer to the head of the list. Then, we traverse the list and reverse the links between the nodes. The intuition behind this approach is to change the next pointer of each node to point to the previous node, effectively reversing the list.

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
        // Initialize previous and current pointers
        ListNode* prev = nullptr;
        ListNode* curr = head;
        
        // Traverse the list and reverse the links
        while (curr != nullptr) {
            // Store the next node
            ListNode* nextTemp = curr->next;
            // Reverse the link
            curr->next = prev;
            // Move the pointers
            prev = curr;
            curr = nextTemp;
        }
        
        // Return the new head of the reversed list
        return prev;
    }
};
```

## Test Cases
```
Input: [1,2,3,4,5]
Output: [5,4,3,2,1]
Input: [1]
Output: [1]
Input: []
Output: []
```

## Key Takeaways
- Initialize three pointers: previous, current, and next to reverse the linked list.
- Change the next pointer of each node to point to the previous node to reverse the list.
- The time complexity is O(n), where n is the number of nodes in the list, and the space complexity is O(1) as we only use a constant amount of space.