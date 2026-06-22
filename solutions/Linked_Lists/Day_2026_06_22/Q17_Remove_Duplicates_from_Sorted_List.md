# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove the duplicates from the sorted list and return the modified list. The list is sorted in ascending order, and each node has a unique identifier. For example, given the list 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, the function should return 1 -> 2 -> 3 -> 4 -> 5. The function should have a time complexity of O(n), where n is the number of nodes in the list, and a space complexity of O(1), as it only uses a constant amount of space.

## Approach
The algorithm uses a two-pointer approach, iterating through the list and skipping duplicate nodes. The current node is compared with the next node, and if they have the same value, the next node is skipped. This process continues until the end of the list is reached.

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
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        // if the list is empty, return NULL
        if (!head) return NULL;
        
        // initialize the current node
        ListNode* current = head;
        
        // iterate through the list
        while (current->next) {
            // if the current node has the same value as the next node, skip the next node
            if (current->val == current->next->val) {
                current->next = current->next->next;
            } else {
                // move to the next node
                current = current->next;
            }
        }
        
        // return the modified list
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
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large lists.
- The use of a two-pointer approach allows for efficient iteration through the list and skipping of duplicate nodes.
- The solution modifies the original list in-place, avoiding the need for extra space.