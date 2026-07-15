# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove the duplicates from the sorted list and return the head of the modified list. The list should be sorted in ascending order. For example, given the list 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, the output should be 1 -> 2 -> 3 -> 4 -> 5. The function should take the head of the list as input and return the head of the modified list.

## Approach
The algorithm iterates through the sorted linked list, comparing each node's value with the next node's value. If the values are the same, the duplicate node is removed. This process continues until all duplicates are removed from the list. The function uses a simple and efficient approach to solve the problem in linear time complexity.

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
        // Initialize the current node
        ListNode* current = head;
        
        // Traverse the linked list
        while (current != NULL && current->next != NULL) {
            // If the current node's value is the same as the next node's value
            if (current->val == current->next->val) {
                // Remove the duplicate node
                current->next = current->next->next;
            } else {
                // Move to the next node
                current = current->next;
            }
        }
        
        // Return the head of the modified list
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
- The function has a time complexity of O(n), where n is the number of nodes in the linked list.
- The function has a space complexity of O(1), as it only uses a constant amount of space to store the current node.
- The function modifies the original linked list by removing duplicate nodes.