# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order, and the resulting list should also be sorted in ascending order. The function should take the heads of the two input lists as input and return the head of the merged list. For example, given two lists `1 -> 3 -> 5` and `2 -> 4 -> 6`, the merged list should be `1 -> 2 -> 3 -> 4 -> 5 -> 6`. The input lists are non-empty, and the nodes have unique values.

## Approach
The algorithm iterates through both lists simultaneously, comparing the current nodes and appending the smaller value to the result list. This process continues until one list is exhausted, at which point the remaining nodes from the other list are appended to the result.

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
        // Create a new dummy node to serve as the head of the result list
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // Iterate through both lists, comparing nodes and appending the smaller value
        while (l1 != NULL && l2 != NULL) {
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
        if (l1 != NULL) {
            current->next = l1;
        } else {
            current->next = l2;
        }
        
        // Return the head of the merged list (excluding the dummy node)
        return dummy->next;
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
- The algorithm has a time complexity of O(n + m), where n and m are the lengths of the input lists.
- The space complexity is O(n + m) due to the creation of a new list.
- The use of a dummy node simplifies the code and avoids special cases for the head of the result list.