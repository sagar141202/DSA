# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order, and the resulting list should also be sorted in ascending order. The function should take the heads of the two lists as input and return the head of the merged list. For example, given two lists `1 -> 3 -> 5` and `2 -> 4 -> 6`, the function should return the head of the list `1 -> 2 -> 3 -> 4 -> 5 -> 6`.

## Approach
The algorithm uses a simple iterative approach to compare nodes from both lists and append the smaller one to the result list. It maintains a dummy node to simplify the code and avoid special handling for the head of the result list. The function iterates through both lists, merging them based on node values.

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
        // Create a dummy node to simplify the code
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // Iterate through both lists and merge them
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
        
        // Append the remaining nodes from either list
        if (l1) {
            current->next = l1;
        } else {
            current->next = l2;
        }
        
        // Return the head of the merged list
        ListNode* head = dummy->next;
        delete dummy;
        return head;
    }
};
```

## Test Cases
```
Input: l1 = [1, 3, 5], l2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
Input: l1 = [], l2 = [0]
Output: [0]
Input: l1 = [1], l2 = []
Output: [1]
```

## Key Takeaways
- Use a dummy node to simplify the code and avoid special handling for the head of the result list.
- Iterate through both lists and merge them based on node values.
- Append the remaining nodes from either list after the iteration is complete.