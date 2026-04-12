# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The linked list has n nodes, and the nodes are numbered from 0 to n - 1. The nodes are connected by a next pointer, and the head represents the first node in the list. The function should return the head of the reversed linked list. For example, if the input linked list is 1 -> 2 -> 3 -> 4 -> 5, the reversed linked list should be 5 -> 4 -> 3 -> 2 -> 1. The constraints are 1 <= n <= 5000, and -5000 <= Node.val <= 5000.

## Approach
The algorithm uses a iterative approach to reverse the linked list by keeping track of the current node and the previous node. It iterates through the list, updating the next pointer of each node to point to the previous node. The intuition is to reverse the direction of the pointers between the nodes.

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
        // Iterate through the list
        while (curr != nullptr) {
            // Store the next node
            ListNode* nextTemp = curr->next;
            // Reverse the next pointer
            curr->next = prev;
            // Move previous and current one step forward
            prev = curr;
            curr = nextTemp;
        }
        // Return the new head
        return prev;
    }
};
```

## Test Cases
```
Input: [1,2,3,4,5]
Output: [5,4,3,2,1]
Input: [1,2]
Output: [2,1]
Input: []
Output: []
```

## Key Takeaways
- Initialize three pointers: previous, current, and next to keep track of the nodes while reversing the list.
- Update the next pointer of the current node to point to the previous node in each iteration.
- Move the previous and current pointers one step forward in each iteration.