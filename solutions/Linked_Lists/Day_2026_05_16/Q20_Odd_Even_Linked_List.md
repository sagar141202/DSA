# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, rearrange the nodes to alternate between odd and even positions. The positions are 1-indexed, meaning the first node is considered odd. The rearranged list should preserve the relative order of nodes within the odd and even positions. For example, given the linked list 1 -> 2 -> 3 -> 4 -> 5, the rearranged list should be 1 -> 3 -> 2 -> 4 -> 5.

## Approach
The solution involves creating two separate linked lists for odd and even nodes and then merging them. We iterate through the original list, appending nodes to either the odd or even list based on their position. Finally, we connect the last node of the odd list to the first node of the even list.

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
        // Base case: if the list is empty or only contains one node
        if (!head || !head->next) return head;

        // Initialize pointers for odd and even lists
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;

        // Iterate through the list
        while (even && even->next) {
            // Update odd pointer
            odd->next = even->next;
            odd = odd->next;

            // Update even pointer
            even->next = odd->next;
            even = even->next;
        }

        // Connect the last node of the odd list to the first node of the even list
        odd->next = evenHead;

        return head;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 3 -> 2 -> 4 -> 5

Input: 2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7
Output: 2 -> 3 -> 1 -> 5 -> 6 -> 4 -> 7
```

## Key Takeaways
- We can solve this problem by creating two separate linked lists for odd and even nodes.
- The time complexity is O(n), where n is the number of nodes in the list, because we only iterate through the list once.
- The space complexity is O(1) because we only use a constant amount of space to store the pointers.