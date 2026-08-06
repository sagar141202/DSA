# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together, followed by the nodes with even indices, and return the modified list. The indices are 1-indexed, meaning the head of the list is considered as the node at index 1. For example, if the input list is 1 -> 2 -> 3 -> 4 -> 5, the output should be 1 -> 3 -> 5 -> 2 -> 4.

## Approach
The algorithm involves creating two separate linked lists, one for odd-indexed nodes and one for even-indexed nodes. We iterate through the original list, appending nodes to the appropriate list based on their index. Finally, we concatenate the two lists to obtain the modified list.

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
        if (!head || !head->next) return head;
        
        // Initialize two pointers, one for the odd list and one for the even list
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;
        
        // Iterate through the list, separating nodes into odd and even lists
        while (even && even->next) {
            odd->next = even->next;
            odd = odd->next;
            even->next = odd->next;
            even = even->next;
        }
        
        // Concatenate the odd and even lists
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
- Separate the linked list into two lists based on node indices.
- Iterate through the list, appending nodes to the appropriate list.
- Concatenate the two lists to obtain the modified list.