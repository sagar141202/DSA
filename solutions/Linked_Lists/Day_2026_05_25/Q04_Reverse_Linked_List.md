# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes' values are in the range [-5000, 5000]. The list is guaranteed to be non-empty, except for the case when the list is empty (i.e., the head is null). For example, if the input is [1, 2, 3, 4, 5], the output should be [5, 4, 3, 2, 1].

## Approach
The approach to solve this problem is to initialize three pointers: previous, current, and next. We traverse the list and reverse the next pointer of each node. The algorithm iterates through the list until it reaches the end, effectively reversing the entire list in one pass.

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
            // Store next node
            ListNode* nextTemp = curr->next;
            // Reverse the link
            curr->next = prev;
            // Move pointers one position ahead
            prev = curr;
            curr = nextTemp;
        }
        // When the loop finishes, 'prev' will be pointing to the new head
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
- We use a simple iterative approach to reverse the linked list, eliminating the need for recursion.
- The algorithm runs in linear time complexity, making it efficient for large lists.
- The space complexity is constant, as we only use a fixed amount of space to store the pointers.