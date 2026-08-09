# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the linked list such that all nodes with a value less than x come before nodes with a value greater than or equal to x. The relative order of the nodes with values less than x and the relative order of the nodes with values greater than or equal to x should be maintained. For example, given a linked list 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, the partitioned linked list should be 1 -> 2 -> 2 -> 4 -> 3 -> 5.

## Approach
The algorithm involves creating two separate linked lists, one for nodes with values less than x and another for nodes with values greater than or equal to x. Then, it concatenates these two lists to form the partitioned linked list. This approach ensures that the relative order of nodes is maintained.

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
        ListNode* beforeDummy = new ListNode(0);
        ListNode* afterDummy = new ListNode(0);
        
        // Initialize the tails of the two lists
        ListNode* before = beforeDummy;
        ListNode* after = afterDummy;
        
        // Traverse the original list
        while (head != nullptr) {
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
        
        // Connect the before list to the after list
        after->next = nullptr;
        before->next = afterDummy->next;
        
        // Return the head of the partitioned list
        ListNode* result = beforeDummy->next;
        delete beforeDummy;
        delete afterDummy;
        return result;
    }
};
```

## Test Cases
```
Input: head = [1, 4, 3, 2, 5, 2], x = 3
Output: [1, 2, 2, 4, 3, 5]
```

## Key Takeaways
- The algorithm uses two dummy nodes to simplify the code and avoid edge cases.
- It maintains the relative order of nodes by only moving nodes between the two lists, without changing their original order.
- The time complexity is O(n), where n is the number of nodes in the linked list, because each node is visited once.