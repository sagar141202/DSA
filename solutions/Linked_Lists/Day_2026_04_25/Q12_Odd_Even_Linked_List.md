# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The indices in this list are **0-indexed**. For example, given a linked list `1 -> 2 -> 3 -> 4 -> 5`, the odd indices are `1 -> 3 -> 5` and the even indices are `2 -> 4`. The modified list should be `1 -> 3 -> 5 -> 2 -> 4`.

## Approach
We can solve this problem by using two separate linked lists to store the nodes with odd and even indices, then combining them at the end. We will iterate over the original list, appending nodes to the correct list based on their index. Finally, we will connect the two lists.

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

        // Initialize two dummy nodes for odd and even lists
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;

        // Iterate over the original list
        while (even != nullptr && even->next != nullptr) {
            // Update odd node's next pointer
            odd->next = even->next;
            odd = odd->next;

            // Update even node's next pointer
            even->next = odd->next;
            even = even->next;
        }

        // Connect the two lists
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
- Separate the nodes into two linked lists based on their indices.
- Use dummy nodes to simplify the code and avoid edge cases.
- Connect the two lists at the end to get the final modified list.