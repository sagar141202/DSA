# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The indices in this problem are 0-indexed, and the first node is considered to have index 0. For example, if the input is 1 -> 2 -> 3 -> 4 -> 5, then the output should be 1 -> 3 -> 5 -> 2 -> 4.

## Approach
The solution involves creating two separate linked lists, one for odd-indexed nodes and one for even-indexed nodes. We then concatenate these two lists to get the final result. This approach ensures that the odd-indexed nodes appear before the even-indexed nodes in the modified list.

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
        if (head == nullptr) return nullptr;
        if (head->next == nullptr) return head;
        
        // Initialize two pointers for odd and even lists
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;
        
        // Traverse the list and separate nodes into odd and even lists
        while (even != nullptr && even->next != nullptr) {
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
- Separate the linked list into two parts: one for odd-indexed nodes and one for even-indexed nodes.
- Use two pointers to traverse the list and separate the nodes into the two lists.
- Concatenate the odd and even lists to get the final result.