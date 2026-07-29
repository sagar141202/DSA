# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes will have values in the range [-5000, 5000]. The list can be empty, and the function should handle this case. For example, given the list 1 -> 2 -> 3 -> 4 -> 5, the function should return 5 -> 4 -> 3 -> 2 -> 1.

## Approach
We can reverse a linked list by iterating over the list and reversing the next pointer of each node. We will keep track of the previous node to correctly reverse the next pointer. This approach will allow us to reverse the list in one pass.

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
        // Initialize previous node to nullptr
        ListNode* prev = nullptr;
        // Initialize current node to head
        ListNode* curr = head;
        // Traverse the list
        while (curr) {
            // Store the next node
            ListNode* nextTemp = curr->next;
            // Reverse the next pointer
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
- Reversing a linked list can be done in one pass by iterating over the list and reversing the next pointer of each node.
- We need to keep track of the previous node to correctly reverse the next pointer.
- The time complexity of this approach is O(n), where n is the number of nodes in the list, and the space complexity is O(1) since we only use a constant amount of space.