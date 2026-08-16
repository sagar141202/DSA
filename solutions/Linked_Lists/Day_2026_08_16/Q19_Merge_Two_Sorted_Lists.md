# Merge Two Sorted Lists

## Problem Statement
Merge two sorted linked lists into one sorted linked list. The lists are sorted in ascending order, and the resulting list should also be sorted in ascending order. For example, given two lists `1 -> 3 -> 5` and `2 -> 4 -> 6`, the merged list should be `1 -> 2 -> 3 -> 4 -> 5 -> 6`. The input lists are defined as singly linked lists, where each node has a value and a pointer to the next node. The function should return the head of the merged list.

## Approach
The algorithm uses a recursive approach to merge the two lists. It compares the values of the current nodes in both lists and adds the smaller value to the merged list. This process continues until one of the lists is exhausted, at which point the remaining nodes from the other list are appended to the merged list.

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
        
        // Continue merging until one of the lists is exhausted
        while (l1 && l2) {
            if (l1->val < l2->val) {
                // Add the smaller value to the merged list
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }
        
        // Append the remaining nodes from the other list
        if (l1) {
            current->next = l1;
        } else {
            current->next = l2;
        }
        
        // Return the head of the merged list (excluding the dummy node)
        return dummy->next;
    }
};
```

## Test Cases
```
Input: l1 = [1, 3, 5], l2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
```

## Key Takeaways
- The time complexity of the solution is O(n + m), where n and m are the lengths of the input lists.
- The space complexity of the solution is O(n + m), as we create a new merged list with the same total number of nodes as the input lists.
- The solution uses a dummy node to simplify the code and avoid special cases for the head of the merged list.