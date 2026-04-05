# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The indices in this list are 0-indexed. For example, if the input is 1 -> 2 -> 3 -> 4 -> 5, the output should be 1 -> 3 -> 5 -> 2 -> 4.

## Approach
We will use two separate linked lists to store the odd and even indexed nodes. We will then merge these two lists to get the final result. The algorithm involves iterating over the input list and appending nodes to the odd and even lists based on their indices.

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
        // Base case: if the list is empty or contains only one node
        if (!head || !head->next) return head;

        // Initialize the odd and even lists
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;

        // Iterate over the input list
        while (even && even->next) {
            // Update the next pointer of the odd node
            odd->next = even->next;
            // Update the next pointer of the even node
            even->next = odd->next->next;
            // Move to the next odd and even nodes
            odd = odd->next;
            even = even->next;
        }

        // Merge the odd and even lists
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
- We can solve this problem by using two separate linked lists to store the odd and even indexed nodes.
- We need to handle the base cases where the input list is empty or contains only one node.
- The time complexity of this solution is O(n), where n is the number of nodes in the input list.