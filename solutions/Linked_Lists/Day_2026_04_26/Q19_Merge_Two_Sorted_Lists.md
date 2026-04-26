# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order. The function should take the heads of the two lists as input and return the head of the merged list. For example, given two lists `1 -> 3 -> 5` and `2 -> 4 -> 6`, the merged list should be `1 -> 2 -> 3 -> 4 -> 5 -> 6`. The lists can be of different lengths.

## Approach
The algorithm uses a recursive approach to merge the two lists by comparing the values of the nodes and adding the smaller one to the result list. The process is repeated until one of the lists is exhausted. The remaining nodes from the non-exhausted list are then appended to the result list.

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
        
        // Merge the two lists
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
        
        // Append the remaining nodes from the non-exhausted list
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
Input: l1 = [1, 2, 3], l2 = []
Output: [1, 2, 3]
Input: l1 = [], l2 = [1, 2, 3]
Output: [1, 2, 3]
```

## Key Takeaways
- The time complexity is O(n + m) where n and m are the lengths of the two lists.
- The space complexity is O(n + m) for the recursive call stack.
- A dummy node can be used to simplify the code and avoid special handling for the head of the merged list.