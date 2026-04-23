# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The input linked lists are sorted in ascending order, and the output linked list should also be sorted in ascending order. For example, given two linked lists `1 -> 2 -> 4` and `1 -> 3 -> 4`, the merged linked list should be `1 -> 1 -> 2 -> 3 -> 4 -> 4`. The linked lists are defined as singly linked lists, where each node has a value and a pointer to the next node.

## Approach
The solution uses a simple iterative approach, comparing the current nodes of the two linked lists and adding the smaller one to the result list. This process continues until one of the linked lists is exhausted, at which point the remaining nodes of the other list are appended to the result.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        // Create a dummy node to simplify the code
        ListNode* dummy = new ListNode();
        ListNode* current = dummy;
        
        // Compare the current nodes of the two linked lists
        while (l1 && l2) {
            if (l1->val < l2->val) {
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }
        
        // Append the remaining nodes of the other list
        if (l1) {
            current->next = l1;
        } else {
            current->next = l2;
        }
        
        // Return the next node of the dummy node
        return dummy->next;
    }
};
```

## Test Cases
```
Input: l1 = [1, 2, 4], l2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
Input: l1 = [], l2 = []
Output: []
Input: l1 = [], l2 = [0]
Output: [0]
```

## Key Takeaways
- Use a dummy node to simplify the code and avoid special cases for the head of the result list.
- Compare the current nodes of the two linked lists and add the smaller one to the result list.
- Append the remaining nodes of the other list once one of the linked lists is exhausted.