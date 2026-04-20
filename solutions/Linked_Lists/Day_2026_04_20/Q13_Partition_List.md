# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the linked list such that all nodes with values less than x come before nodes with values greater than or equal to x. The relative order of the nodes with values less than x and the relative order of the nodes with values greater than or equal to x should be maintained. The list should be modified in-place.

## Approach
We will use two separate linked lists to store the nodes with values less than x and the nodes with values greater than or equal to x. Then, we will connect the two lists to form the final partitioned list. This approach ensures the relative order of the nodes is maintained.

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
        // Create two dummy nodes to simplify the code
        ListNode* beforeDummy = new ListNode();
        ListNode* afterDummy = new ListNode();
        
        // Initialize the current pointers
        ListNode* before = beforeDummy;
        ListNode* after = afterDummy;
        
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
            // Move to the next node in the original list
            head = head->next;
        }
        
        // Connect the before and after lists
        after->next = nullptr;
        before->next = afterDummy->next;
        
        // Return the head of the partitioned list
        return beforeDummy->next;
    }
};
```

## Test Cases
```
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
```

## Key Takeaways
- Use two separate lists to store nodes with values less than x and nodes with values greater than or equal to x.
- Connect the two lists to form the final partitioned list while maintaining the relative order of nodes.
- Use dummy nodes to simplify the code and avoid edge cases.