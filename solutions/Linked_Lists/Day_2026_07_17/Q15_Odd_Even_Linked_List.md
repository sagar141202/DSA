# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The indices in this list are 0-indexed. For example, if the input is `1 -> 2 -> 3 -> 4 -> 5 -> 6`, the output will be `1 -> 3 -> 5 -> 2 -> 4 -> 6`. The relative order inside both the even and odd groups should remain as it was in the original list.

## Approach
The algorithm involves separating the linked list into two lists: one for odd-indexed nodes and one for even-indexed nodes. We then concatenate these two lists. This can be achieved by maintaining two pointers for the odd and even lists and rearranging the nodes accordingly.

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
        // Base cases
        if (!head) return head;
        if (!head->next) return head;
        if (!head->next->next) return head;

        // Initialize pointers
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;

        // Traverse the list
        while (even && even->next) {
            odd->next = even->next;
            odd = odd->next;
            even->next = odd->next;
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

Input: 2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7
Output: 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4
```

## Key Takeaways
- The solution has a time complexity of O(n), where n is the number of nodes in the linked list.
- The space complexity is O(1), as we only use a constant amount of space to store the pointers.
- The relative order of nodes within the odd and even groups is preserved, as required by the problem statement.