# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove duplicates from the list and return the head of the modified list. The list is sorted in ascending order, and each node has a unique identifier. For example, if the input list is 1 -> 1 -> 2 -> 3 -> 3 -> 4, the output should be 1 -> 2 -> 3 -> 4. The function should handle cases where the input list is empty or contains a single node.

## Approach
The algorithm iterates through the linked list, comparing each node's value with the next node's value. If the values are equal, the next node is skipped. The function uses a pointer to keep track of the current node and updates it accordingly. This approach ensures that duplicates are removed while preserving the original order of the list.

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
            // If the current node's value is equal to the next node's value
            if (current->val == current->next->val) {
                // Remove the next node
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
Input: 1 -> 1 -> 2 -> 3 -> 3 -> 4
Output: 1 -> 2 -> 3 -> 4

Input: 1 -> 2 -> 3 -> 4
Output: 1 -> 2 -> 3 -> 4

Input: 1 -> 1 -> 1 -> 1
Output: 1
```

## Key Takeaways
- The algorithm has a time complexity of O(n), where n is the number of nodes in the linked list.
- The space complexity is O(1) since only a constant amount of space is used to store the current node and other variables.
- The solution uses a two-pointer approach, with the current node and the next node being compared and updated accordingly.