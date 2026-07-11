# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The list is defined as a sequence of nodes, where each node has a value and a pointer to the next node. The function should take the head of the list as input and return the head of the reversed list. For example, if the input list is 1 -> 2 -> 3 -> 4 -> 5, the output should be 5 -> 4 -> 3 -> 2 -> 1.

## Approach
The algorithm iterates through the linked list, keeping track of the current node and the previous node. It then reverses the link between the current node and the next node by updating the next pointer of the current node to point to the previous node. This process is repeated until the end of the list is reached.

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
            // Store the next node
            ListNode* nextTemp = curr->next;
            // Reverse the link
            curr->next = prev;
            // Move to the next node
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
Input: []
Output: []
Input: [1]
Output: [1]
```

## Key Takeaways
- Reversing a linked list can be done iteratively by keeping track of the current and previous nodes.
- The time complexity of this approach is linear, making it efficient for large lists.
- The space complexity is constant, as only a few variables are used to store the nodes.