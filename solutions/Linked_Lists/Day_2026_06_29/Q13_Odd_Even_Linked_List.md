# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The indices in this problem are 0-indexed, i.e., the first node has an index of 0. For example, if the input linked list is `1 -> 2 -> 3 -> 4 -> 5 -> 6`, the output will be `1 -> 3 -> 5 -> 2 -> 4 -> 6`.

## Approach
The algorithm involves creating two separate linked lists, one for odd-indexed nodes and one for even-indexed nodes. We then append the even list to the end of the odd list. This approach ensures that all odd-indexed nodes come before the even-indexed nodes in the resulting list.

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
        // Handle edge cases
        if (head == NULL || head->next == NULL) {
            return head;
        }

        // Initialize pointers for odd and even lists
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;

        // Traverse the list, separating odd and even nodes
        while (even != NULL && even->next != NULL) {
            odd->next = even->next;
            odd = odd->next;
            even->next = odd->next;
            even = even->next;
        }

        // Append the even list to the end of the odd list
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
- Separate the linked list into two lists: one for odd-indexed nodes and one for even-indexed nodes.
- Append the even list to the end of the odd list to get the final result.
- The solution has a time complexity of O(n), where n is the number of nodes in the linked list, and a space complexity of O(1), as it only uses a constant amount of space.