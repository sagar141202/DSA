# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes' values are in the range [-5000, 5000]. The list is guaranteed to be non-null, but it may be empty. For example, if the input is [1, 2, 3, 4, 5], the output should be [5, 4, 3, 2, 1].

## Approach
We will use a iterative approach to reverse the linked list, keeping track of the previous node and reversing the next pointer of each node. This approach allows us to reverse the list in a single pass. We initialize three pointers: previous, current, and next. We traverse the list, and for each node, we do the following: store the next node in next, reverse the link of the current node, and move the previous and current pointers one step forward.

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
        // Initialize previous, current and next pointers
        ListNode* prev = nullptr;
        ListNode* curr = head;
        // Traverse the list
        while (curr != nullptr) {
            // Store next node
            ListNode* nextTemp = curr->next;
            // Reverse current node's pointer
            curr->next = prev;
            // Move pointers one position ahead
            prev = curr;
            curr = nextTemp;
        }
        // Update the head pointer to the new head node
        head = prev;
        return head;
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
- Reversing a linked list can be done iteratively or recursively.
- The iterative approach is generally more efficient than the recursive approach.
- When reversing a linked list, it's essential to keep track of the previous node to correctly reverse the links.