# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified linked list. The indices in this problem are 0-indexed, and the first node is considered to be at index 0. For example, if the linked list is 1 -> 2 -> 3 -> 4 -> 5, the modified linked list will be 1 -> 3 -> 5 -> 2 -> 4.

## Approach
The algorithm involves traversing the linked list and separating the nodes into two lists: one for odd indices and one for even indices. We can use two pointers to keep track of the current nodes in the odd and even lists. We then reconnect the nodes to form the modified linked list.

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

        // Traverse the linked list
        while (even != nullptr && even->next != nullptr) {
            // Update odd pointer
            odd->next = even->next;
            odd = odd->next;

            // Update even pointer
            even->next = odd->next;
            even = even->next;
        }

        // Connect the odd and even lists
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
- We can solve this problem by using two pointers to separate the nodes into two lists.
- We need to handle edge cases where the linked list has less than two nodes.
- The time complexity is O(n), where n is the number of nodes in the linked list, and the space complexity is O(1) since we only use a constant amount of space.