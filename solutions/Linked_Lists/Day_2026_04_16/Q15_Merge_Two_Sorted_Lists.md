# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order, and the merged list should also be sorted in ascending order. The function should take the heads of the two linked lists as input and return the head of the merged linked list. For example, given two linked lists `1 -> 3 -> 5` and `2 -> 4 -> 6`, the merged linked list should be `1 -> 2 -> 3 -> 4 -> 5 -> 6`. The linked lists can be of different lengths, and the function should handle this case. The function should also handle the case where one or both of the input linked lists are empty.

## Approach
The algorithm will use a recursive approach, comparing the values of the nodes in the two linked lists and adding the smaller value to the merged list. The function will continue this process until one of the linked lists is empty, at which point it will append the remaining nodes from the non-empty list to the merged list. This approach ensures that the merged list is sorted in ascending order.

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
        // Create a dummy node to serve as the head of the merged list
        ListNode* dummy = new ListNode();
        ListNode* current = dummy;
        
        // Continue merging nodes until one of the lists is empty
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
        
        // Append the remaining nodes from the non-empty list
        if (l1 != nullptr) {
            current->next = l1;
        } else {
            current->next = l2;
        }
        
        // Return the head of the merged list (which is the next node of the dummy node)
        return dummy->next;
    }
};
```

## Test Cases
```
Input: l1 = [1, 3, 5], l2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
Input: l1 = [], l2 = [1, 3, 5]
Output: [1, 3, 5]
Input: l1 = [1, 3, 5], l2 = []
Output: [1, 3, 5]
```

## Key Takeaways
- The function uses a recursive approach to compare the values of the nodes in the two linked lists.
- The function handles the case where one or both of the input linked lists are empty.
- The time complexity is O(n + m), where n and m are the lengths of the two linked lists.