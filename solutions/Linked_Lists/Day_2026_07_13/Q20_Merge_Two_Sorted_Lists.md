# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order. The function should take the heads of the two lists as input and return the head of the merged list. For example, if the input lists are 1 -> 3 -> 5 and 2 -> 4 -> 6, the output should be 1 -> 2 -> 3 -> 4 -> 5 -> 6. The lists can be of different lengths.

## Approach
The algorithm iterates through both lists, comparing the current nodes and adding the smaller one to the merged list. This process continues until one list is exhausted, at which point the remaining nodes from the other list are appended to the merged list. The function uses a dummy node to simplify the code and avoid special cases for the head of the merged list.

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
        
        // Iterate through both lists
        while (l1 != NULL && l2 != NULL) {
            // Compare the current nodes and add the smaller one to the merged list
            if (l1->val < l2->val) {
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }
        
        // Append the remaining nodes from the other list
        if (l1 != NULL) {
            current->next = l1;
        } else {
            current->next = l2;
        }
        
        // Return the head of the merged list
        return dummy->next;
    }
};
```

## Test Cases
```
Input: l1 = 1 -> 3 -> 5, l2 = 2 -> 4 -> 6
Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
Input: l1 = 1 -> 2 -> 3, l2 = NULL
Output: 1 -> 2 -> 3
Input: l1 = NULL, l2 = 1 -> 2 -> 3
Output: 1 -> 2 -> 3
```

## Key Takeaways
- Use a dummy node to simplify the code and avoid special cases for the head of the merged list.
- Iterate through both lists, comparing the current nodes and adding the smaller one to the merged list.
- Append the remaining nodes from the other list once one list is exhausted.