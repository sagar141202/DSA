# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the linked list such that all nodes with values less than x come before nodes with values greater than or equal to x. The relative order of the nodes with values less than x and the relative order of the nodes with values greater than or equal to x should be preserved. The list should be modified in-place.

## Approach
We will use two dummy nodes to create two separate lists, one for values less than x and one for values greater than or equal to x. We will then traverse the original list and append each node to the corresponding list. Finally, we will connect the two lists.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        // Create two dummy nodes
        ListNode* before = new ListNode();
        ListNode* after = new ListNode();
        
        // Initialize two pointers
        ListNode* beforeHead = before;
        ListNode* afterHead = after;
        
        // Traverse the original list
        while (head) {
            // If the current node's value is less than x
            if (head->val < x) {
                // Append the node to the before list
                before->next = head;
                before = before->next;
            } else {
                // Append the node to the after list
                after->next = head;
                after = after->next;
            }
            // Move to the next node
            head = head->next;
        }
        
        // Connect the two lists
        after->next = nullptr;
        before->next = afterHead->next;
        
        // Return the head of the modified list
        return beforeHead->next;
    }
};
```

## Test Cases
```
Input: [1, 4, 3, 2, 5, 2], x = 3
Output: [1, 2, 2, 4, 3, 5]
```

## Key Takeaways
- We use two dummy nodes to simplify the code and avoid edge cases.
- We traverse the original list only once, making the time complexity O(n).
- We only use a constant amount of space, making the space complexity O(1).