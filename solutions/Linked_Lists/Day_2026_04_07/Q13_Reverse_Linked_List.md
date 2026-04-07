# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes' values are in the range [-5000, 5000]. The list is non-empty and consists of nodes with unique values. For example, if the input linked list is 1 -> 2 -> 3 -> 4 -> 5, the reversed linked list should be 5 -> 4 -> 3 -> 2 -> 1.

## Approach
The algorithm uses a three-pointer technique to reverse the linked list. We initialize three pointers: previous, current, and next. We traverse the list, updating the next pointer of each node to point to the previous node. This process is repeated until we reach the end of the list.

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
        // Traverse the list
        while (curr) {
            // Store next node
            ListNode* nextTemp = curr->next;
            // Reverse the link
            curr->next = prev;
            // Move pointers one position ahead
            prev = curr;
            curr = nextTemp;
        }
        // At the end, prev will be the new head
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
- Reversing a linked list can be done in O(n) time complexity and O(1) space complexity.
- The three-pointer technique is useful for reversing linked lists.
- It's essential to update the next pointer of each node correctly to avoid losing any nodes during the reversal process.