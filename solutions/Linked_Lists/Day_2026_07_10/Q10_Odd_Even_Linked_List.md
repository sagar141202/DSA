# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, separate the nodes into two lists: one containing all the nodes with odd indices and the other containing all the nodes with even indices. The nodes in both lists should be in the same relative order as they were in the original list. The indices are 0-indexed. For example, if the original list is 1 -> 2 -> 3 -> 4 -> 5 -> 6, the odd list should be 1 -> 3 -> 5 and the even list should be 2 -> 4 -> 6. Return the head of the odd list.

## Approach
The approach is to create two separate linked lists, one for odd indices and one for even indices, and then merge them. We can use two pointers to keep track of the current nodes in both lists. We will iterate through the original list, appending nodes to the odd or even list based on their index.

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
    ListNode* oddEvenList(ListNode* head) {
        // If the list is empty, return the head
        if (!head) return head;
        
        // Initialize two pointers, one for the odd list and one for the even list
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;
        
        // Iterate through the list
        while (even && even->next) {
            // Update the next pointer for the odd node
            odd->next = even->next;
            // Update the next pointer for the even node
            even->next = odd->next->next;
            // Move to the next nodes
            odd = odd->next;
            even = even->next;
        }
        
        // Connect the odd list to the even list
        odd->next = evenHead;
        
        return head;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6
Output: 1 -> 3 -> 5 -> 2 -> 4 -> 6
```

## Key Takeaways
- We use two pointers to keep track of the current nodes in the odd and even lists.
- We iterate through the original list, updating the next pointers for the odd and even nodes.
- We connect the odd list to the even list at the end to maintain the relative order of the nodes.