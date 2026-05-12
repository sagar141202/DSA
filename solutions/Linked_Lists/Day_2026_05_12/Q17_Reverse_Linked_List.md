# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes' values are in the range [-5000, 5000]. The list can be empty, and the nodes can have duplicate values. For example, if the input linked list is 1 -> 2 -> 3 -> 4 -> 5, the output should be 5 -> 4 -> 3 -> 2 -> 1.

## Approach
We will use a simple iterative approach to reverse the linked list, keeping track of the current node and the previous node. We will update the next pointer of each node to point to the previous node. This process will be repeated until we reach the end of the list.

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
        // Traverse the list
        while (curr != NULL) {
            // Store next node
            ListNode* nextTemp = curr->next;
            // Reverse the link
            curr->next = prev;
            // Move forward in list
            prev = curr;
            curr = nextTemp;
        }
        // New head is the last non-NULL node we visited
        return prev;
    }
};
```

## Test Cases
```
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
Input: []
Output: []
Input: [1]
Output: [1]
```

## Key Takeaways
- We only need to keep track of the current node and the previous node to reverse the linked list.
- The time complexity is O(n), where n is the number of nodes in the list, because we visit each node once.
- The space complexity is O(1) because we only use a constant amount of space to store the previous node and the current node.