# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes have values in the range [-5000, 5000]. The list is guaranteed to be non-null. For example, if the input linked list is 1 -> 2 -> 3 -> 4 -> 5, the output should be 5 -> 4 -> 3 -> 2 -> 1.

## Approach
The algorithm uses a iterative approach to reverse the linked list by keeping track of the previous node and updating the next pointer of each node. This process continues until all nodes have been traversed. The new head of the reversed list is the last node visited.

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
        // Initialize previous node as NULL
        ListNode* prev = NULL;
        // Initialize current node as head
        ListNode* curr = head;
        // Traverse the linked list
        while (curr) {
            // Store the next node
            ListNode* nextTemp = curr->next;
            // Reverse the link
            curr->next = prev;
            // Move forward in list
            prev = curr;
            // Move forward in list
            curr = nextTemp;
        }
        // New head is the last node visited
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
- Reversing a linked list can be done iteratively or recursively.
- It's essential to keep track of the previous node to update the next pointer correctly.
- The time complexity for reversing a linked list is O(n), where n is the number of nodes in the list.