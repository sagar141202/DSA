# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove the duplicates from the sorted list and return the head of the modified list. The list should remain sorted after removal of duplicates. For example, if the input list is 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, the output should be 1 -> 2 -> 3 -> 4 -> 5.

## Approach
We can iterate through the list and compare each node with its next node. If the values are the same, we skip the next node by changing the next pointer of the current node. This approach ensures that the list remains sorted after removal of duplicates. We only need to traverse the list once, making it efficient.

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
        // Initialize current node as head
        ListNode* current = head;
        
        // Traverse the list
        while (current != NULL && current->next != NULL) {
            // If current node's value is the same as next node's value
            if (current->val == current->next->val) {
                // Skip the next node
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
- The solution has a time complexity of O(n) where n is the number of nodes in the list.
- The solution has a space complexity of O(1) as it only uses a constant amount of space to store the current node.
- The solution modifies the original list by changing the next pointers of the nodes.