# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The indices in this problem are 0-indexed. For example, if the input is 1 -> 2 -> 3 -> 4 -> 5, the output should be 1 -> 3 -> 5 -> 2 -> 4.

## Approach
The approach is to create two separate linked lists, one for odd indices and one for even indices. We will then combine these two lists to get the final result. This can be achieved by maintaining two pointers, one for the odd list and one for the even list.

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
        // Base case: if the list is empty or only contains one node, return the head
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        // Initialize two pointers, one for the odd list and one for the even list
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;

        // Traverse the list
        while (even != nullptr && even->next != nullptr) {
            // Update the next pointer of the odd node to skip the even node
            odd->next = even->next;
            // Update the next pointer of the even node to skip the odd node
            even->next = odd->next->next;
            // Move the odd and even pointers
            odd = odd->next;
            even = even->next;
        }

        // Combine the two lists
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
- We can solve this problem by creating two separate linked lists, one for odd indices and one for even indices.
- We need to maintain two pointers, one for the odd list and one for the even list, to traverse the list and combine the two lists.
- The time complexity is O(n), where n is the number of nodes in the list, and the space complexity is O(1) since we only use a constant amount of space.