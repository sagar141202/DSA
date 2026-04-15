# Linked List Cycle

## Problem Statement
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle is when a node's next pointer points back to a previous node. The function should return true if a cycle is present and false otherwise. The linked list may have multiple nodes with the same value, so a cycle should be determined by the node's memory address, not its value. The function should run in O(n) time and use O(1) space, where n is the number of nodes in the linked list. For example, given the linked list 3 -> 2 -> 0 -> -4 -> 2, the function should return true because the last node's next pointer points to the second node.

## Approach
We can use Floyd's Tortoise and Hare algorithm to detect a cycle in the linked list. The algorithm uses two pointers, one that moves one step at a time and one that moves two steps at a time. If a cycle is present, the two pointers will eventually meet.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        // If the linked list is empty, there's no cycle
        if (head == NULL || head->next == NULL) {
            return false;
        }
        
        // Initialize two pointers, one that moves one step at a time and one that moves two steps at a time
        ListNode *tortoise = head;
        ListNode *hare = head->next;
        
        // Move the pointers through the linked list
        while (tortoise != hare) {
            // If the hare reaches the end of the linked list, there's no cycle
            if (hare == NULL || hare->next == NULL) {
                return false;
            }
            
            // Move the tortoise one step
            tortoise = tortoise->next;
            
            // Move the hare two steps
            hare = hare->next->next;
        }
        
        // If the tortoise and hare meet, there's a cycle
        return true;
    }
};
```

## Test Cases
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the last node's next pointer points to the second node.

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the last node's next pointer points to the first node.

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

## Key Takeaways
- Floyd's Tortoise and Hare algorithm can be used to detect a cycle in a linked list in O(n) time and O(1) space.
- The algorithm uses two pointers, one that moves one step at a time and one that moves two steps at a time, to detect if a cycle is present.
- If the two pointers meet, a cycle is present in the linked list.