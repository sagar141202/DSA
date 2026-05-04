# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes' values are in the range [-5000, 5000]. The list can be empty, and the list can have duplicate values. For example, if the input linked list is 1 -> 2 -> 3 -> 4 -> 5, the output should be 5 -> 4 -> 3 -> 2 -> 1.

## Approach
We will use a iterative approach to reverse the linked list, keeping track of the previous node to correctly reverse the links. This approach will allow us to reverse the list in a single pass. We will use three pointers: previous, current, and next.

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
        // Initialize previous as NULL
        ListNode* prev = NULL;
        // Initialize current as head
        ListNode* curr = head;
        // Traverse the list
        while (curr != NULL) {
            // Store next node
            ListNode* next = curr->next;
            // Reverse the link
            curr->next = prev;
            // Move previous and current one step forward
            prev = curr;
            curr = next;
        }
        // Return the new head node
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
- The key to this problem is to keep track of the previous node to correctly reverse the links.
- We use three pointers: previous, current, and next to traverse the list and reverse the links.
- This solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for large lists.