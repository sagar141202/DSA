# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order, and the task is to create a new sorted list containing all elements from both input lists. The input lists are defined as singly linked lists, where each node has a value and a pointer to the next node. The goal is to merge these lists while maintaining the sorted order. For example, given two lists 1 -> 3 -> 5 and 2 -> 4 -> 6, the merged list should be 1 -> 2 -> 3 -> 4 -> 5 -> 6.

## Approach
The algorithm involves creating a new linked list and iteratively adding the smaller element from the front of the two input lists. This process continues until all elements from both lists are incorporated into the new list. The key to this solution is comparing the current nodes of the two lists and appending the smaller value to the new list.

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
        // Create a dummy node to simplify the merging process
        ListNode* dummy = new ListNode();
        ListNode* current = dummy;
        
        // Continue merging until one list is exhausted
        while (l1 && l2) {
            // Compare the current nodes of the two lists
            if (l1->val < l2->val) {
                // Append the smaller value to the new list
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }
            // Move to the next position in the new list
            current = current->next;
        }
        
        // Append any remaining nodes from the non-exhausted list
        if (l1) {
            current->next = l1;
        } else {
            current->next = l2;
        }
        
        // Return the merged list (excluding the dummy node)
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
- Iterative comparison and appending of smaller elements is key to merging sorted linked lists efficiently.
- Using a dummy node simplifies the code by avoiding special cases for the head of the merged list.
- The solution has a linear time complexity due to the single pass through both input lists.