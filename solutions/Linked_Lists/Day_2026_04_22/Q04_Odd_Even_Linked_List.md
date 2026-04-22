# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The indices in this list are 0-indexed, i.e., the first node has an index of 0, the second node has an index of 1, and so on. The odd and even indices are determined based on the original list, not the rearranged list. For example, if the original list is 1 -> 2 -> 3 -> 4 -> 5 -> 6, then the odd nodes will be 1 -> 3 -> 5 and the even nodes will be 2 -> 4 -> 6. The modified list will be 1 -> 3 -> 5 -> 2 -> 4 -> 6.

## Approach
The solution involves creating two separate linked lists, one for odd-indexed nodes and one for even-indexed nodes, and then merging them. We iterate over the original list, appending odd-indexed nodes to the odd list and even-indexed nodes to the even list. Finally, we connect the two lists.

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
        // Base case
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        // Initialize odd and even lists
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;

        // Traverse the list and separate odd and even nodes
        while (even != nullptr && even->next != nullptr) {
            // Update odd node's next pointer
            odd->next = even->next;
            odd = odd->next;

            // Update even node's next pointer
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
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6
Output: 1 -> 3 -> 5 -> 2 -> 4 -> 6

Input: 2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7
Output: 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4
```

## Key Takeaways
- Separate the linked list into two lists, one for odd-indexed nodes and one for even-indexed nodes.
- Connect the two lists to form the modified list.
- The time complexity is O(n), where n is the number of nodes in the list, and the space complexity is O(1) since we only use a constant amount of space.