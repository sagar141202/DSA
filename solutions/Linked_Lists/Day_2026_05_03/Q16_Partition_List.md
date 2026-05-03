# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the linked list such that all nodes with a value less than x come before all nodes with a value greater than or equal to x. The relative order of the nodes with values less than x and the relative order of the nodes with values greater than or equal to x should be maintained. The list should be modified in-place.

## Approach
The algorithm uses two separate linked lists to store nodes with values less than x and greater than or equal to x. It iterates through the original list, appending each node to the appropriate list. Finally, it concatenates the two lists.

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
        // Create two dummy nodes to simplify the code
        ListNode* beforeHead = new ListNode(0);
        ListNode* afterHead = new ListNode(0);
        
        // Initialize the tails of the two lists
        ListNode* before = beforeHead;
        ListNode* after = afterHead;
        
        // Iterate through the original list
        while (head) {
            // If the current node's value is less than x, append it to the before list
            if (head->val < x) {
                before->next = head;
                before = before->next;
            } 
            // Otherwise, append it to the after list
            else {
                after->next = head;
                after = after->next;
            }
            head = head->next;
        }
        
        // Set the next of the last node in the after list to nullptr
        after->next = nullptr;
        
        // Concatenate the two lists
        before->next = afterHead->next;
        
        // Return the head of the modified list
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
```

## Key Takeaways
- The algorithm maintains the relative order of nodes within the two partitions.
- It uses two separate linked lists to simplify the partitioning process.
- The time complexity is O(n), where n is the number of nodes in the linked list, because each node is visited exactly once.