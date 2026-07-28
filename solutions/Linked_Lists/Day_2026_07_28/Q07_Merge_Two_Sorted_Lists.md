# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order, and the resulting list should also be sorted in ascending order. For example, given two lists `1 -> 3 -> 5` and `2 -> 4 -> 6`, the merged list should be `1 -> 2 -> 3 -> 4 -> 5 -> 6`. The input lists are defined as follows: each node in the list has an integer value and a pointer to the next node in the list. The input lists are not empty, and each node's value is unique.

## Approach
The algorithm uses a recursive approach to merge the two sorted lists by comparing the current nodes of both lists and appending the smaller value to the result list. This process continues until one list is exhausted, at which point the remaining nodes from the other list are appended to the result.

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
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        // Create a new dummy node to serve as the start of the result list
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // Merge smaller elements first
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
        
        // If there are remaining nodes in either list, append them to the result
        if (l1) {
            current->next = l1;
        } else if (l2) {
            current->next = l2;
        }
        
        // Return the next node of the dummy node, which is the start of the result list
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
- The time complexity is O(n + m) because we visit each node in both lists once.
- The space complexity is O(n + m) because we create a new list with n + m nodes in the worst case.