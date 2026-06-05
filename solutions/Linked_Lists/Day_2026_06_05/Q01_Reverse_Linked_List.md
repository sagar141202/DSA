# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes' values are in the range [-5000, 5000]. The list can be empty (i.e., the head is null). For example, if the input list is 1 -> 2 -> 3 -> 4 -> 5, the output should be 5 -> 4 -> 3 -> 2 -> 1.

## Approach
The algorithm uses a simple iterative approach to reverse the linked list by changing the next pointer of each node. It initializes three pointers: previous, current, and next. The previous pointer is used to keep track of the previous node, and the next pointer is used to temporarily store the next node.

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
        
        // Traverse the linked list
        while (curr != nullptr) {
            // Store the next node
            ListNode* nextTemp = curr->next;
            
            // Reverse the link
            curr->next = prev;
            
            // Move the pointers
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
- Reversing a linked list can be done in O(n) time complexity where n is the number of nodes in the list.
- We only need a constant amount of space to store the previous, current, and next pointers, making the space complexity O(1).
- The key to solving this problem is to keep track of the previous node and update the next pointer of each node accordingly.