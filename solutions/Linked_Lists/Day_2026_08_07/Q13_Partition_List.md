# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the list such that all nodes with values less than x come before nodes with values greater than or equal to x. The relative order of the nodes should be preserved. For example, given a list 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, the partitioned list should be 1 -> 2 -> 2 -> 4 -> 3 -> 5.

## Approach
The algorithm involves creating two separate linked lists: one for nodes with values less than x and another for nodes with values greater than or equal to x. Then, it combines these two lists while preserving the relative order of nodes.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
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
    ListNode* partition(ListNode* head, int x) {
        // Create two dummy nodes for the two lists
        ListNode* beforeHead = new ListNode(0);
        ListNode* afterHead = new ListNode(0);
        
        // Initialize the tails of the two lists
        ListNode* before = beforeHead;
        ListNode* after = afterHead;
        
        // Traverse the original list
        while (head) {
            // If the current node's value is less than x, add it to the before list
            if (head->val < x) {
                before->next = head;
                before = before->next;
            } 
            // Otherwise, add it to the after list
            else {
                after->next = head;
                after = after->next;
            }
            head = head->next;
        }
        
        // Combine the two lists
        after->next = nullptr;
        before->next = afterHead->next;
        
        // Return the head of the partitioned list
        ListNode* result = beforeHead->next;
        delete beforeHead;
        delete afterHead;
        return result;
    }
};
```

## Test Cases
```
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Input: head = [2,1], x = 2
Output: [1,2]
```

## Key Takeaways
- Use two separate linked lists to store nodes with values less than x and greater than or equal to x.
- Preserve the relative order of nodes by traversing the original list and adding nodes to the correct lists.
- Combine the two lists by setting the next pointer of the last node in the before list to the head of the after list.