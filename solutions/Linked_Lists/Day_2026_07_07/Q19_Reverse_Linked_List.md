# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The list's nodes have values ranging from -5000 to 5000. For example, if the input is 1 -> 2 -> 3 -> 4 -> 5, the output should be 5 -> 4 -> 3 -> 2 -> 1.

## Approach
We will use a simple iterative approach to reverse the linked list. We initialize three pointers: previous, current, and next. We traverse the list, and for each node, we reverse the next pointer.

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
        // Initialize previous, current, and next pointers
        ListNode* prev = nullptr;
        ListNode* curr = head;
        // Traverse the list
        while (curr != nullptr) {
            // Store next node
            ListNode* nextTemp = curr->next;
            // Reverse the link
            curr->next = prev;
            // Move pointers one step forward
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
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
Input: [1, 2]
Output: [2, 1]
Input: []
Output: []
```

## Key Takeaways
- We use three pointers (previous, current, and next) to reverse the linked list.
- The time complexity is O(n) where n is the number of nodes in the list.
- The space complexity is O(1) as we only use a constant amount of space.