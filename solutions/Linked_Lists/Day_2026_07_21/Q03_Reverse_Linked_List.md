# Reverse Linked List

## Problem Statement
Given the head of a singly linked list, reverse the list and return the reversed list. The number of nodes in the list is in the range [0, 5000]. The nodes' values are in the range [-5000, 5000]. The list can be empty, and it is guaranteed that the input list is a valid singly linked list. For example, if the input list is 1 -> 2 -> 3 -> 4 -> 5, the output should be 5 -> 4 -> 3 -> 2 -> 1.

## Approach
The approach is to initialize three pointers: previous, current, and next. We start with the current pointer at the head of the list and the previous pointer as NULL. Then, we traverse the list, updating the next pointer of each node to point to the previous node. This process effectively reverses the links between the nodes.

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
        // Initialize previous pointer as NULL
        ListNode* prev = NULL;
        // Initialize current pointer at the head of the list
        ListNode* curr = head;
        
        // Traverse the list
        while (curr != NULL) {
            // Store the next node
            ListNode* nextTemp = curr->next;
            // Reverse the link
            curr->next = prev;
            // Move the pointers one step forward
            prev = curr;
            curr = nextTemp;
        }
        
        // At the end, 'prev' will be pointing to the new head of the reversed list
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
- We only need to keep track of the previous node to reverse the list, hence the space complexity is O(1).
- Reversing a linked list can be done in a single pass, resulting in a time complexity of O(n), where n is the number of nodes in the list.
- The key to solving linked list problems often lies in properly managing the pointers and understanding how the nodes are connected.