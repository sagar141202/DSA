# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order, and the task is to create a new sorted linked list containing all elements from both lists. The function should take the heads of the two linked lists as input and return the head of the merged linked list. For example, given two lists 1 -> 3 -> 5 and 2 -> 4 -> 6, the function should return 1 -> 2 -> 3 -> 4 -> 5 -> 6. The lists can be of different lengths.

## Approach
The algorithm iterates through both linked lists simultaneously, comparing the current nodes and adding the smaller value to the new list. This process continues until all nodes from both lists are merged. The function uses a dummy node to simplify the merging process.

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
        
        // Iterate through both linked lists
        while (l1 != nullptr && l2 != nullptr) {
            // Compare the current nodes and add the smaller value to the new list
            if (l1->val < l2->val) {
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }
        
        // Add any remaining nodes from either list
        if (l1 != nullptr) {
            current->next = l1;
        } else {
            current->next = l2;
        }
        
        // Return the head of the merged linked list
        return dummy->next;
    }
};
```

## Test Cases
```
Input: l1 = [1, 3, 5], l2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
```

## Key Takeaways
- The function uses a dummy node to simplify the merging process and avoid special handling for the head of the merged list.
- The algorithm iterates through both linked lists simultaneously, comparing the current nodes and adding the smaller value to the new list.
- The time complexity is O(n + m), where n and m are the lengths of the input linked lists.