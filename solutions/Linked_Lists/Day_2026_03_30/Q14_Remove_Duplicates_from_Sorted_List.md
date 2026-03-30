# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove the duplicates from the sorted list. The function should take the head of the list as input and return the head of the modified list. The list is sorted in ascending order, and all duplicate nodes should be removed. For example, if the input list is 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, the output should be 1 -> 2 -> 3 -> 4 -> 5.

## Approach
The algorithm involves iterating through the linked list and comparing each node with its next node. If the values are the same, the next node is skipped by updating the next pointer of the current node. This process continues until all duplicate nodes are removed.

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
    ListNode* deleteDuplicates(ListNode* head) {
        // if the list is empty, return nullptr
        if (!head) return nullptr;
        
        // initialize the current node
        ListNode* current = head;
        
        // iterate through the list
        while (current->next) {
            // if the current node and the next node have the same value
            if (current->val == current->next->val) {
                // skip the next node
                current->next = current->next->next;
            } else {
                // move to the next node
                current = current->next;
            }
        }
        
        // return the head of the modified list
        return head;
    }
};
```

## Test Cases
```
Input: 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5
Input: 1 -> 1 -> 1 -> 1 -> 1
Output: 1
```

## Key Takeaways
- The function iterates through the linked list only once, resulting in a time complexity of O(n).
- The function only uses a constant amount of space to store the current node, resulting in a space complexity of O(1).
- The function modifies the original list by updating the next pointers of the nodes, rather than creating a new list.