# Remove Duplicates from Sorted List

## Problem Statement
Given the head of a sorted linked list, remove duplicates from the list and return the head of the modified list. The list should remain sorted after removal of duplicates. For example, if the input list is 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5, the output should be 1 -> 2 -> 3 -> 4 -> 5. The list nodes are defined as follows: 
```cpp
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
```
The function to be implemented should take the head of the list as input and return the head of the modified list.

## Approach
The approach is to traverse the list and compare each node's value with the next node's value. If the values are the same, skip the next node by updating the current node's next pointer. This process continues until the end of the list is reached.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        // If the list is empty, return nullptr
        if (!head) return nullptr;
        
        // Initialize the current node
        ListNode* current = head;
        
        // Traverse the list
        while (current->next) {
            // If the current node's value is the same as the next node's value
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
- Traverse the list and compare each node's value with the next node's value to remove duplicates.
- Update the current node's next pointer to skip the next node if the values are the same.
- The time complexity is O(n) where n is the number of nodes in the list, and the space complexity is O(1) as only a constant amount of space is used.