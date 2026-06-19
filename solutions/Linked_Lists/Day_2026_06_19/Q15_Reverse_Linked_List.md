# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes are numbered from 0 to n - 1, where n is the number of nodes. The nodes have values in the range [-5000, 5000]. The list is defined as a sequence of nodes, where each node has a value and a next pointer pointing to the next node in the sequence. The task is to reverse the direction of the pointers so that the last node points to the second last node, the second last node points to the third last node, and so on, until the first node points to null.

## Approach
The approach is to initialize three pointers, previous, current, and next, and traverse the linked list. In each iteration, we reverse the next pointer of the current node to point to the previous node. We then move the previous and current pointers one step forward.

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
        // Initialize previous pointer to nullptr
        ListNode* prev = nullptr;
        // Initialize current pointer to head
        ListNode* curr = head;
        // Traverse the linked list
        while (curr != nullptr) {
            // Store the next node
            ListNode* nextTemp = curr->next;
            // Reverse the next pointer of the current node
            curr->next = prev;
            // Move the previous and current pointers one step forward
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
Input: [1,2]
Output: [2,1]
Input: []
Output: []
```

## Key Takeaways
- We use three pointers, previous, current, and next, to traverse the linked list and reverse the next pointers.
- We initialize the previous pointer to nullptr and the current pointer to the head of the list.
- We return the new head of the reversed list, which is the last node we visited.