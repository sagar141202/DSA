# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, rearrange the nodes to alternate between the nodes that were originally at odd indices and the nodes that were originally at even indices. The rearranged list should still be a singly linked list, and the relative order of the nodes at odd and even indices should be preserved. For example, if the original list is 1 -> 2 -> 3 -> 4 -> 5, the rearranged list should be 1 -> 3 -> 5 -> 2 -> 4.

## Approach
The algorithm involves iterating over the linked list and separating the nodes at odd and even indices into two separate lists. Then, it combines these two lists to form the final rearranged linked list. This can be achieved by maintaining two pointers for the odd and even lists.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        // Base case
        if (head == NULL || head->next == NULL) {
            return head;
        }

        // Initialize pointers for odd and even lists
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;

        // Traverse the linked list
        while (even != NULL && even->next != NULL) {
            // Update odd list
            odd->next = even->next;
            odd = odd->next;

            // Update even list
            even->next = odd->next;
            even = even->next;
        }

        // Combine odd and even lists
        odd->next = evenHead;

        return head;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 3 -> 5 -> 2 -> 4
Input: 2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7
Output: 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4
```

## Key Takeaways
- The problem can be solved by separating the nodes at odd and even indices into two lists and then combining them.
- The time complexity is linear because we only traverse the linked list once.
- The space complexity is constant because we only use a constant amount of space to store the pointers.