# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove the duplicates from the sorted list such that each element appears only once. The relative order of the elements should be kept the same. The list is sorted in ascending order. For example, if the input list is 1 -> 1 -> 2 -> 3 -> 3 -> 4, the output should be 1 -> 2 -> 3 -> 4.

## Approach
The approach is to iterate over the linked list and compare each node with its next node. If the values are the same, we skip the next node. We use a pointer to keep track of the last non-duplicate node.

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
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        // if the list is empty, return head
        if (!head) return head;
        
        // initialize two pointers
        ListNode* current = head;
        
        // iterate over the list
        while (current->next) {
            // if the current node's value is the same as the next node's value
            if (current->val == current->next->val) {
                // skip the next node
                current->next = current->next->next;
            } else {
                // move to the next node
                current = current->next;
            }
        }
        
        // return the head of the modified list
        return head;
    }
};
```

## Test Cases
```
Input: 1 -> 1 -> 2 -> 3 -> 3 -> 4
Output: 1 -> 2 -> 3 -> 4
Input: 1 -> 1 -> 1 -> 1 -> 1
Output: 1
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5
```

## Key Takeaways
- We can remove duplicates from a sorted linked list in O(n) time complexity.
- We only need to keep track of the last non-duplicate node to solve this problem.
- This solution has a space complexity of O(1) as we are not using any extra space.