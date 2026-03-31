# Reverse Linked List

## Problem Statement
Reverse a singly linked list. The linked list is defined as a sequence of nodes, where each node contains an integer value and a reference (i.e., "link") to the next node in the sequence. This is a fundamental data structure problem, and the goal is to write a function that takes the head of the list as input and returns the head of the reversed list. For example, given the list 1 -> 2 -> 3 -> 4 -> 5, the function should return the head of the list 5 -> 4 -> 3 -> 2 -> 1.

## Approach
The algorithm to reverse a linked list involves initializing three pointers: previous, current, and next. We traverse the list, and for each node, we update the next pointer to point to the previous node, effectively reversing the link. This process continues until we reach the end of the list.

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
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (curr != nullptr) {
            ListNode* nextTemp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextTemp;
        }
        return prev;
    }
};
```

## Test Cases
```
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
Input: [1]
Output: [1]
Input: []
Output: []
```

## Key Takeaways
- Initialize three pointers: previous, current, and next, to keep track of the nodes during the reversal process.
- Traverse the list and update the next pointer of each node to point to the previous node, effectively reversing the link.
- The function returns the head of the reversed list, which is the last non-null node encountered during the traversal.