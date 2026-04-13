# Linked List Cycle II

## Problem Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return nullptr. The linked list has at least one node, and all the values are unique. The cycle begins at some node and ends at the same node. For example, given the linked list 3 -> 2 -> 0 -> -4 -> 2, the cycle begins at the second node.

## Approach
We can use the Floyd's Tortoise and Hare algorithm to detect the cycle in the linked list. Once the cycle is detected, we reset one of the pointers to the head of the list and move both pointers one step at a time to find the start of the cycle.

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
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (head == nullptr || head->next == nullptr) {
            return nullptr;
        }
        
        ListNode *slow = head;
        ListNode *fast = head;
        
        // Detect cycle using Floyd's Tortoise and Hare algorithm
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
            
            if (slow == fast) {
                break;
            }
        }
        
        if (fast == nullptr || fast->next == nullptr) {
            return nullptr;
        }
        
        // Reset slow pointer to head and move both pointers one step at a time
        slow = head;
        while (slow != fast) {
            slow = slow->next;
            fast = fast->next;
        }
        
        return slow;
    }
};
```

## Test Cases
```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Input: head = [1], pos = -1
Output: no cycle
```

## Key Takeaways
- Use Floyd's Tortoise and Hare algorithm to detect the cycle in the linked list.
- Once the cycle is detected, reset one of the pointers to the head of the list and move both pointers one step at a time to find the start of the cycle.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), where n is the number of nodes in the linked list.