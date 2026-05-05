# Reorder List

## Problem Statement
Given the head of a singly linked list, reorder the list such that the first node becomes the first node of the reordered list, the last node becomes the second node, the second node becomes the third node, and so on. The problem assumes that the linked list has at least one node and the nodes are 1-indexed. The solution should be implemented in a way that it only uses O(1) extra space, excluding the space required for the output.

## Approach
To solve this problem, we can use a three-step approach: find the middle of the linked list, reverse the second half of the list, and then merge the two halves. This approach ensures that we are reordering the list as required.

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
    void reorderList(ListNode* head) {
        // Base case
        if (!head || !head->next || !head->next->next) {
            return;
        }

        // Find the middle of the list
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Reverse the second half of the list
        ListNode* second = slow->next;
        slow->next = nullptr;
        ListNode* prev = nullptr;
        while (second) {
            ListNode* temp = second->next;
            second->next = prev;
            prev = second;
            second = temp;
        }

        // Merge the two halves
        ListNode* first = head;
        second = prev;
        while (second) {
            ListNode* temp1 = first->next;
            ListNode* temp2 = second->next;
            first->next = second;
            second->next = temp1;
            first = temp1;
            second = temp2;
        }
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4
Output: 1 -> 4 -> 2 -> 3
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 5 -> 2 -> 4 -> 3
```

## Key Takeaways
- To solve linked list problems, it's essential to understand the different operations like insertion, deletion, and reversal.
- Reversing a linked list can be done in-place by keeping track of the previous node.
- Merging two linked lists can be done by adjusting the next pointers of the nodes.