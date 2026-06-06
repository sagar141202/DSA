# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order, and the merged list should also be sorted in ascending order. The function should take the heads of the two linked lists as input and return the head of the merged linked list. For example, given two linked lists `1 -> 3 -> 5` and `2 -> 4 -> 6`, the merged linked list should be `1 -> 2 -> 3 -> 4 -> 5 -> 6`. The input linked lists can be empty, and the function should handle this case correctly.

## Approach
The algorithm uses a recursive approach to merge the two linked lists. It compares the values of the nodes at the current positions in the two lists and adds the smaller value to the merged list. The function then moves to the next nodes in the lists and repeats the process until one of the lists is exhausted. The remaining nodes in the other list are then added to the merged list.

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
        // Create a new dummy node to serve as the head of the merged list
        ListNode* dummy = new ListNode();
        ListNode* current = dummy;
        
        // While both lists have nodes
        while (l1 && l2) {
            // If the current node in l1 has a smaller value, add it to the merged list
            if (l1->val < l2->val) {
                current->next = l1;
                l1 = l1->next;
            } 
            // Otherwise, add the current node in l2 to the merged list
            else {
                current->next = l2;
                l2 = l2->next;
            }
            // Move to the next node in the merged list
            current = current->next;
        }
        
        // Add any remaining nodes in l1 or l2 to the merged list
        if (l1) {
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
Input: l1 = [], l2 = [2, 4, 6]
Output: [2, 4, 6]
Input: l1 = [1, 3, 5], l2 = []
Output: [1, 3, 5]
```

## Key Takeaways
- The function uses a recursive approach to merge the two linked lists.
- The time complexity is O(n + m), where n and m are the lengths of the input linked lists.
- The space complexity is O(n + m), as the function creates a new linked list with n + m nodes.