# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order, and the resulting list should also be sorted in ascending order. For example, given two lists `1 -> 2 -> 4` and `1 -> 3 -> 4`, the merged list should be `1 -> 1 -> 2 -> 3 -> 4 -> 4`. The input lists are defined by their node values and `next` pointers. The function should return the head of the merged list.

## Approach
We can solve this problem using a recursive approach or an iterative approach. The idea is to compare the node values of the two lists and add the smaller value to the merged list. We will use an iterative approach for simplicity and efficiency.

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
        // Create a new dummy node to simplify the code
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // Iterate through both lists
        while (l1 != NULL && l2 != NULL) {
            // Compare the node values and add the smaller value to the merged list
            if (l1->val < l2->val) {
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }
            // Move to the next node in the merged list
            current = current->next;
        }
        
        // Add any remaining nodes from either list
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
Input: l1 = [1, 2, 4], l2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
Input: l1 = [], l2 = [0]
Output: [0]
Input: l1 = [1], l2 = []
Output: [1]
```

## Key Takeaways
- We can solve this problem using either a recursive or iterative approach.
- The time complexity is O(n + m), where n and m are the lengths of the input lists.
- The space complexity is O(n + m) for the recursive approach, but O(1) for the iterative approach (excluding the space needed for the output).