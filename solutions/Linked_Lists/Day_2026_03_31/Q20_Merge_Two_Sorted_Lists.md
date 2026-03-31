# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order, and the nodes have a value and a pointer to the next node. The function should return the head of the merged linked list. For example, given two lists `1 -> 3 -> 5` and `2 -> 4 -> 6`, the merged list should be `1 -> 2 -> 3 -> 4 -> 5 -> 6`. The lists can be empty, and the function should handle this case correctly.

## Approach
The algorithm uses a recursive approach to merge the two lists by comparing the values of the current nodes and appending the smaller value to the merged list. The function continues this process until one of the lists is empty, at which point it appends the remaining nodes from the other list. This approach ensures that the merged list is also sorted in ascending order.

## Complexity
- Time: O(n + m)
- Space: O(n + m)

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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        // Create a dummy node to serve as the head of the merged list
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;

        // Merge the two lists
        while (l1 != NULL && l2 != NULL) {
            if (l1->val < l2->val) {
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }

        // Append the remaining nodes from the non-empty list
        if (l1 != NULL) {
            current->next = l1;
        } else {
            current->next = l2;
        }

        // Return the head of the merged list (excluding the dummy node)
        ListNode* head = dummy->next;
        delete dummy;
        return head;
    }
};
```

## Test Cases
```
Input: l1 = [1, 3, 5], l2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
Input: l1 = [], l2 = [1, 2, 3]
Output: [1, 2, 3]
Input: l1 = [1, 2, 3], l2 = []
Output: [1, 2, 3]
```

## Key Takeaways
- The function uses a recursive approach to merge the two sorted linked lists.
- It creates a dummy node to serve as the head of the merged list and avoids edge cases.
- The time complexity is O(n + m), where n and m are the lengths of the input lists.