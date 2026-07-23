# Odd Even Linked List

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the modified list. The first node is considered odd, and the second node is even, and so on. Note that the relative order inside both the even and odd groups should remain as it was in the original list. For example, if the given list is 1 -> 2 -> 3 -> 4 -> 5 -> 6, the modified list should be 1 -> 3 -> 5 -> 2 -> 4 -> 6.

## Approach
The algorithm involves creating two separate linked lists, one for odd-indexed nodes and one for even-indexed nodes. We then concatenate these two lists to get the final result. This approach ensures that the relative order inside both groups remains as it was in the original list.

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
        // Base case: if the list has 0 or 1 node, return the list as it is
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        // Initialize two pointers, one for the odd list and one for the even list
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;

        // Traverse the list, rearranging nodes as we go
        while (even != nullptr && even->next != nullptr) {
            // Update the next pointer of the odd node to skip the even node
            odd->next = even->next;
            // Update the next pointer of the even node to skip the next odd node
            even->next = odd->next->next;
            // Move the odd and even pointers two steps forward
            odd = odd->next;
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
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6
Output: 1 -> 3 -> 5 -> 2 -> 4 -> 6
```

## Key Takeaways
- We use two separate linked lists to group odd and even indexed nodes.
- The relative order inside both groups remains as it was in the original list.
- The time complexity is O(n), where n is the number of nodes in the list, and the space complexity is O(1) since we only use a constant amount of space.