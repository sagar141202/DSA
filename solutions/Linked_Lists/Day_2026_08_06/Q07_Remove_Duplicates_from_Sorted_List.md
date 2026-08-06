# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove the duplicates from the sorted list so that each element appears only once. The relative order of the elements should be kept the same. For example, given the sorted linked list `1 -> 1 -> 2 -> 3 -> 3`, the function should return `1 -> 2 -> 3`. The linked list is sorted in ascending order and the nodes have a value and a pointer to the next node.

## Approach
The approach to solve this problem is to traverse the linked list and compare the current node's value with the next node's value. If they are the same, we skip the next node. This is done by changing the `next` pointer of the current node to the node after the next node. We repeat this process until we reach the end of the linked list.

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
        // Initialize the current node
        ListNode* current = head;
        
        // Traverse the linked list
        while (current != nullptr && current->next != nullptr) {
            // If the current node's value is the same as the next node's value
            if (current->val == current->next->val) {
                // Skip the next node
                current->next = current->next->next;
            } else {
                // Move to the next node
                current = current->next;
            }
        }
        
        // Return the head of the modified linked list
        return head;
    }
};
```

## Test Cases
```
Input: 1 -> 1 -> 2 -> 3 -> 3
Output: 1 -> 2 -> 3
Input: 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5
Input: 1 -> 1 -> 1 -> 1 -> 1
Output: 1
```

## Key Takeaways
- We can solve this problem in O(n) time complexity where n is the number of nodes in the linked list.
- We only need to use a constant amount of space to store the current node, so the space complexity is O(1).
- The relative order of the elements is preserved after removing the duplicates.