# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes' values are in the range [-5000, 5000]. The list is guaranteed to be non-circular. For example, if the input linked list is 1 -> 2 -> 3 -> 4 -> 5, the output should be 5 -> 4 -> 3 -> 2 -> 1.

## Approach
The algorithm uses a simple iterative approach to reverse the linked list by keeping track of the previous node and updating the next pointer of each node. This process continues until the end of the list is reached. The new head of the reversed list is the last node in the original list.

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
        // Initialize previous node as nullptr
        ListNode* prev = nullptr;
        // Initialize current node as head
        ListNode* curr = head;
        // Traverse the list
        while (curr != nullptr) {
            // Store next node
            ListNode* nextTemp = curr->next;
            // Reverse the link
            curr->next = prev;
            // Move forward in list
            prev = curr;
            curr = nextTemp;
        }
        // New head is the last node
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
- Use a previous node to keep track of the reversed list.
- Update the next pointer of each node to reverse the list.
- The new head of the reversed list is the last node in the original list.