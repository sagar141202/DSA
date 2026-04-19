# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The indices in this list are 1-indexed. For example, if the input is 1->2->3->4->5, the output should be 1->3->5->2->4. The relative order inside both the even and odd groups should remain as it was in the original list.

## Approach
The solution involves iterating over the linked list and separating the nodes into two lists: one for odd indices and one for even indices. We can achieve this by maintaining two separate lists and then concatenating them.

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
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        // If the list is empty or has only one node, return it as it is
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        // Initialize two pointers, one for the odd list and one for the even list
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;

        // Iterate over the list
        while (even != nullptr && even->next != nullptr) {
            // Update the next pointer of the odd node to skip the even node
            odd->next = even->next;
            // Update the next pointer of the even node to skip the next odd node
            even->next = odd->next->next;
            // Move the odd and even pointers two steps forward
            odd = odd->next;
            even = even->next;
        }

        // Concatenate the even list to the end of the odd list
        odd->next = evenHead;
        return head;
    }
};
```

## Test Cases
```
Input: 1->2->3->4->5
Output: 1->3->5->2->4
Input: 2->1->3->5->6->4->7
Output: 2->3->6->7->1->5->4
```

## Key Takeaways
- Separate the nodes into two lists: one for odd indices and one for even indices.
- Use two pointers to iterate over the list and update the next pointers accordingly.
- Concatenate the even list to the end of the odd list to get the final modified list.