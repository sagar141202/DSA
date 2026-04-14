# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order, and the task is to create a new list that contains all elements from both lists in sorted order. For example, given two lists 1 -> 3 -> 5 and 2 -> 4 -> 6, the merged list should be 1 -> 2 -> 3 -> 4 -> 5 -> 6. The input lists can be of varying lengths, and the solution should handle cases where one or both lists are empty.

## Approach
The approach involves creating a new list and iterating through both input lists, comparing the current nodes and appending the smaller value to the new list. This process continues until all nodes from both lists have been processed. The algorithm uses a dummy node to simplify the code and avoid special handling for the head of the new list.

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
        
        // Append any remaining nodes from either list
        if (l1 != NULL) {
            current->next = l1;
        } else {
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
Input: l1 = [], l2 = [1, 2, 3]
Output: [1, 2, 3]
Input: l1 = [1, 2, 3], l2 = []
Output: [1, 2, 3]
```

## Key Takeaways
- The solution uses a dummy node to simplify the code and avoid special handling for the head of the new list.
- The time complexity is O(n + m), where n and m are the lengths of the input lists, because we process each node exactly once.
- The space complexity is O(n + m) because we create a new list that contains all nodes from both input lists.