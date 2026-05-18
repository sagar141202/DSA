# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes' values are in the range [-5000, 5000]. The list is defined as a sequence of nodes, where each node has a value and a reference (i.e., "next") to the next node in the sequence. This sequence is terminated by null. For example, the sequence 1 -> 2 -> 3 can be represented as a linked list where each node contains a value (1, 2, or 3) and a reference to the next node. Reversing this list results in the sequence 3 -> 2 -> 1.

## Approach
We can reverse the linked list by initializing three pointers: previous, current, and next. We then traverse the list, updating the next pointer of each node to point to the previous node. This process effectively reverses the links between nodes.

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
        // Initialize previous pointer
        ListNode* prev = nullptr;
        // Initialize current pointer
        ListNode* curr = head;
        // Traverse the list
        while (curr != nullptr) {
            // Store the next node
            ListNode* nextTemp = curr->next;
            // Reverse the link
            curr->next = prev;
            // Move pointers one step forward
            prev = curr;
            curr = nextTemp;
        }
        // Return the new head (which is the last non-null node)
        return prev;
    }
};
```

## Test Cases
```
Input: [1,2,3,4,5]
Output: [5,4,3,2,1]
Input: []
Output: []
Input: [1]
Output: [1]
```

## Key Takeaways
- To reverse a linked list, we need to update the next pointer of each node to point to the previous node.
- We use three pointers (previous, current, and next) to keep track of the nodes during the reversal process.
- The time complexity of this solution is O(n), where n is the number of nodes in the list, because we are traversing the list once.
- The space complexity is O(1) because we only use a constant amount of space to store the pointers.