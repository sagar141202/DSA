# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order, and the merged list should also be sorted in ascending order. The function should take the heads of the two linked lists as input and return the head of the merged linked list. For example, if the first list is 1 -> 3 -> 5 and the second list is 2 -> 4 -> 6, the merged list should be 1 -> 2 -> 3 -> 4 -> 5 -> 6.

## Approach
The algorithm uses a recursive approach to merge the two sorted linked lists. It compares the values of the nodes of the two lists and adds the smaller value to the merged list. This process is repeated until one of the lists is exhausted. The remaining nodes of the other list are then added to the merged list.

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
        
        // Merge the two lists
        while (l1 != nullptr && l2 != nullptr) {
            if (l1->val < l2->val) {
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }
        
        // Add the remaining nodes of the other list
        if (l1 != nullptr) {
            current->next = l1;
        } else {
            current->next = l2;
        }
        
        // Return the head of the merged list
        return dummy->next;
    }
};
```

## Test Cases
```
Input: l1 = [1, 3, 5], l2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
Input: l1 = [], l2 = [0]
Output: [0]
Input: l1 = [], l2 = []
Output: []
```

## Key Takeaways
- The time complexity of the solution is O(n + m), where n and m are the lengths of the two linked lists.
- The space complexity of the solution is O(n + m), as we need to create a new linked list to store the merged result.
- The solution uses a dummy node to simplify the merging process and avoid special handling for the head of the merged list.