# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order, and the task is to create a new list that contains all elements from both lists in ascending order. For example, given two lists `1 -> 3 -> 5` and `2 -> 4 -> 6`, the merged list should be `1 -> 2 -> 3 -> 4 -> 5 -> 6`. The input lists are non-empty, and each node in the list has a unique value.

## Approach
The approach is to use a simple iterative method to compare nodes from both lists and append the smaller node to the result list. This process continues until all nodes from both lists are exhausted. The algorithm uses a dummy node to simplify the code.

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
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // Iterate through both lists and compare nodes
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
        
        // Append the remaining nodes, if any
        if (l1) {
            current->next = l1;
        } else if (l2) {
            current->next = l2;
        }
        
        // Return the merged list (excluding the dummy node)
        ListNode* result = dummy->next;
        delete dummy;
        return result;
    }
};
```

## Test Cases
```
Input: l1 = [1, 3, 5], l2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
Input: l1 = [1, 2, 3], l2 = []
Output: [1, 2, 3]
Input: l1 = [], l2 = [1, 2, 3]
Output: [1, 2, 3]
```

## Key Takeaways
- Use a dummy node to simplify the code and avoid special handling for the head node.
- Iterate through both lists and compare nodes to determine the correct order.
- Append the remaining nodes, if any, to the merged list.