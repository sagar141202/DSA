# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The indices in this list are **0-indexed**. For example, given a linked list `1 -> 2 -> 3 -> 4 -> 5`, the odd nodes are `1 -> 3 -> 5` and the even nodes are `2 -> 4`. You should return `1 -> 3 -> 5 -> 2 -> 4`.

## Approach
The approach involves separating the linked list into two lists: one for odd-indexed nodes and one for even-indexed nodes. We then append the even list to the end of the odd list. This is achieved by maintaining two pointers for the odd and even lists.

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
    ListNode* oddEvenList(ListNode* head) {
        // Handle edge cases
        if (!head) return head;
        if (!head->next) return head;
        if (!head->next->next) return head;

        // Initialize pointers
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;

        // Traverse the list
        while (even && even->next) {
            odd->next = even->next;  // Link odd node to next odd node
            odd = odd->next;         // Move to next odd node
            even->next = odd->next;  // Link even node to next even node
            even = even->next;       // Move to next even node
        }

        // Link the end of odd list to the start of even list
        odd->next = evenHead;

        return head;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 3 -> 5 -> 2 -> 4
```

## Key Takeaways
- The problem can be solved by separating the linked list into two lists and then appending one to the other.
- The use of two pointers (one for the odd list and one for the even list) simplifies the solution and reduces space complexity.
- The time complexity remains linear as we only traverse the list once.