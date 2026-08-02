# Partition List

## Problem Statement
Given the head of a linked list and a value x, partition the linked list such that all nodes with values less than x come before nodes with values greater than or equal to x. The relative order of the nodes with values less than x and the relative order of the nodes with values greater than or equal to x should be maintained. For example, given a linked list 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3, the partitioned list should be 1 -> 2 -> 2 -> 4 -> 3 -> 5.

## Approach
The algorithm involves creating two separate linked lists, one for nodes with values less than x and another for nodes with values greater than or equal to x. We then concatenate these two lists to obtain the final partitioned list. This approach ensures that the relative order of nodes within each partition is maintained.

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
        // Create two dummy nodes to serve as the heads of the two lists
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
        
        // Connect the before list to the after list
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
- We use two dummy nodes to simplify the code and avoid dealing with null pointer exceptions.
- The relative order of nodes within each partition is maintained by appending nodes to the end of each list.
- The time complexity is O(n), where n is the number of nodes in the linked list, since we traverse the list once. The space complexity is O(1), excluding the space required for the output, since we only use a constant amount of space to store the dummy nodes and the tails of the two lists.