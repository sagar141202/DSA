# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes' values are in the range [-5000, 5000]. The list is guaranteed to be non-empty, except for the case where the list is empty. For example, if the input is [1, 2, 3, 4, 5], the output should be [5, 4, 3, 2, 1].

## Approach
We will use a simple iterative approach to reverse the linked list by keeping track of the previous node and updating the next pointer of each node. This approach only requires a single pass through the list. We will initialize three pointers: previous, current, and next.

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
        // Initialize previous and current pointers
        ListNode* prev = nullptr;
        ListNode* curr = head;
        
        // Traverse the list and reverse the links
        while (curr != nullptr) {
            // Store the next node
            ListNode* nextTemp = curr->next;
            
            // Reverse the link
            curr->next = prev;
            
            // Move the pointers one step forward
            prev = curr;
            curr = nextTemp;
        }
        
        // At the end, 'prev' will be the new head of the reversed list
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
- We only need to traverse the list once to reverse it.
- It's essential to keep track of the previous node to update the next pointer correctly.
- The time complexity is linear, and the space complexity is constant, making this solution efficient for large lists.