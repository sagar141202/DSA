# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes' values are in the range [-5000, 5000]. The list is guaranteed to be non-null, but the head may be null. For example, given the linked list 1 -> 2 -> 3 -> 4 -> 5, the reversed linked list should be 5 -> 4 -> 3 -> 2 -> 1.

## Approach
We can solve this problem by initializing three pointers: previous, current, and next. We initialize the previous pointer to null and the current pointer to the head of the list. Then, we traverse the list, updating the next pointer of each node to point to the previous node.

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
        // Initialize previous pointer to null
        ListNode* prev = nullptr;
        // Initialize current pointer to the head of the list
        ListNode* curr = head;
        // Traverse the list
        while (curr != nullptr) {
            // Store the next node
            ListNode* nextTemp = curr->next;
            // Reverse the link
            curr->next = prev;
            // Move pointers one position ahead
            prev = curr;
            curr = nextTemp;
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
Input: [1, 2]
Output: [2, 1]
Input: []
Output: []
```

## Key Takeaways
- We use three pointers (previous, current, and next) to reverse the linked list.
- The time complexity of this solution is O(n), where n is the number of nodes in the linked list.
- The space complexity of this solution is O(1), as we only use a constant amount of space to store the pointers.