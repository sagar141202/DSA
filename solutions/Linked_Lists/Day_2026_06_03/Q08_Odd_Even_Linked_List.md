# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The indices in this problem are 0-indexed. For example, if the input list is 1 -> 2 -> 3 -> 4 -> 5, then the output should be 1 -> 3 -> 5 -> 2 -> 4.

## Approach
The solution involves creating two separate linked lists, one for odd-indexed nodes and one for even-indexed nodes, then merging them. We can achieve this by maintaining two pointers for the odd and even lists and iterating through the original list.

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
        // Base case: if the list is empty or has only one node
        if (!head || !head->next) return head;

        // Initialize two pointers, one for the odd list and one for the even list
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;

        // Iterate through the list
        while (even && even->next) {
            // Update the next pointer of the odd node to the next odd node
            odd->next = even->next;
            // Update the next pointer of the even node to the next even node
            even->next = odd->next->next;
            // Move the odd and even pointers forward
            odd = odd->next;
            even = even->next;
        }

        // Merge the odd and even lists
        odd->next = evenHead;

        // Return the modified list
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
- We can solve this problem by maintaining two separate linked lists for odd and even indices.
- The time complexity is linear because we only traverse the list once.
- The space complexity is constant because we only use a constant amount of space to store the pointers.