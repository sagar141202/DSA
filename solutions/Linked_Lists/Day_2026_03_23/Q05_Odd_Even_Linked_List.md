# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The indices in this problem are 0-indexed, and the first node is considered to have index 0. For example, if the input is 1 -> 2 -> 3 -> 4 -> 5, then the output should be 1 -> 3 -> 5 -> 2 -> 4.

## Approach
The algorithm involves iterating over the linked list and separating the nodes into two lists: one for odd indices and one for even indices. We can achieve this by maintaining two pointers for the odd and even lists. We then concatenate the odd list with the even list to obtain the final result.

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
        // Handle edge cases
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        // Initialize pointers for odd and even lists
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;

        // Iterate over the linked list
        while (even != nullptr && even->next != nullptr) {
            // Update odd pointer
            odd->next = even->next;
            odd = odd->next;

            // Update even pointer
            even->next = odd->next;
            even = even->next;
        }

        // Concatenate odd list with even list
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
- We can solve this problem by maintaining two pointers for the odd and even lists.
- The time complexity is O(n), where n is the number of nodes in the linked list.
- The space complexity is O(1), as we only use a constant amount of space to store the pointers.