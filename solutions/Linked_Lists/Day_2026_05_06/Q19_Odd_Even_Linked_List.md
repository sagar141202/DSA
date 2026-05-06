# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The indices in this problem are 0-indexed, and the odd and even indices are grouped separately as if the nodes were in an array. For example, if the input linked list is 1 -> 2 -> 3 -> 4 -> 5, the odd indexed nodes are 1 (0th index) and 3 (2nd index) and the even indexed nodes are 2 (1st index) and 4 (3rd index) and 5 (4th index). The resulting linked list should be 1 -> 3 -> 2 -> 4 -> 5.

## Approach
The approach to solve this problem is to create two separate linked lists, one for odd indexed nodes and one for even indexed nodes, and then merge them. We can use two pointers to keep track of the current nodes in the odd and even linked lists.

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
        if (!head) return head;
        
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;
        
        while (even && even->next) {
            odd->next = even->next;
            odd = odd->next;
            even->next = odd->next;
            even = even->next;
        }
        
        odd->next = evenHead;
        return head;
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 3 -> 2 -> 4 -> 5
```

## Key Takeaways
- We can solve the problem by creating two separate linked lists for odd and even indexed nodes.
- We use two pointers to keep track of the current nodes in the odd and even linked lists.
- The time complexity of the solution is O(n), where n is the number of nodes in the linked list.