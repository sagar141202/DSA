# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order, and the nodes have a value and a pointer to the next node. The function should return the head of the merged linked list. For example, given two lists `1 -> 3 -> 5` and `2 -> 4 -> 6`, the function should return `1 -> 2 -> 3 -> 4 -> 5 -> 6`. The input lists are non-empty, and the nodes have unique values.

## Approach
The algorithm uses a recursive approach to merge the two sorted lists. It compares the values of the nodes at the current positions in the two lists and adds the smaller value to the merged list. The function then moves to the next node in the list with the smaller value. This process continues until one of the lists is exhausted, at which point the remaining nodes from the other list are added to the merged list.

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
        // Create a new dummy node to serve as the head of the merged list
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
        
        // Add the remaining nodes from the non-exhausted list
        if (l1 != NULL) {
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
Input: l1 = [1, 2, 3], l2 = []
Output: [1, 2, 3]
Input: l1 = [], l2 = [1, 2, 3]
Output: [1, 2, 3]
```

## Key Takeaways
- The function uses a recursive approach to merge the two sorted lists, but an iterative approach can also be used for better performance.
- The time complexity is O(n + m), where n and m are the lengths of the two input lists.
- The space complexity is O(n + m) due to the creation of a new merged list.