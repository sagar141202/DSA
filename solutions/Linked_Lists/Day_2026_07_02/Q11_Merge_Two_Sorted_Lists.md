# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order, and the merged list should also be sorted in ascending order. The function should take the heads of the two lists as input and return the head of the merged list. For example, if the first list is 1 -> 3 -> 5 and the second list is 2 -> 4 -> 6, the merged list should be 1 -> 2 -> 3 -> 4 -> 5 -> 6. The function should handle cases where one or both lists are empty.

## Approach
The algorithm uses a recursive approach to merge the two lists by comparing the values of the nodes and appending the smaller value to the result list. The function continues to merge the lists until one of the lists is empty. The algorithm ensures that the resulting list is sorted in ascending order.

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
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        // Create a dummy node to simplify the merging process
        ListNode* dummy = new ListNode();
        ListNode* current = dummy;
        
        // Continue merging until one of the lists is empty
        while (l1 && l2) {
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
        if (l1) {
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
Input: l1 = [], l2 = [2, 4, 6]
Output: [2, 4, 6]
Input: l1 = [1, 3, 5], l2 = []
Output: [1, 3, 5]
```

## Key Takeaways
- The algorithm uses a dummy node to simplify the merging process and avoid special handling for the head of the merged list.
- The time complexity is O(n + m), where n and m are the lengths of the input lists, because each node is visited once.
- The space complexity is O(n + m) because in the worst case, the merged list will contain all nodes from both input lists.