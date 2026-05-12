# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the intersection point of the two lists. The intersection point is the node where the two lists merge. If the lists do not intersect, return nullptr. The lists are non-circular and may have different lengths. For example, given two lists 4 -> 1 -> 8 -> 4 -> 5 and 5 -> 0 -> 1 -> 8 -> 4 -> 5, the intersection point is the node with value 8.

## Approach
The algorithm uses two pointers to traverse both lists. The pointers are moved at the same pace, and when one pointer reaches the end of its list, it is redirected to the start of the other list. This way, if there is an intersection, the pointers will eventually meet at the intersection point.

## Complexity
- Time: O(m + n)
- Space: O(1)

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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        // Initialize two pointers
        ListNode *pA = headA;
        ListNode *pB = headB;
        
        // Traverse both lists
        while (pA != pB) {
            // If pA reaches the end of list A, redirect it to list B
            if (pA == NULL) {
                pA = headB;
            } else {
                pA = pA->next;
            }
            
            // If pB reaches the end of list B, redirect it to list A
            if (pB == NULL) {
                pB = headA;
            } else {
                pB = pB->next;
            }
        }
        
        // If the lists do not intersect, return nullptr
        return pA;
    }
};
```

## Test Cases
```
Input: 
List A: 4 -> 1 -> 8 -> 4 -> 5
List B: 5 -> 0 -> 1 -> 8 -> 4 -> 5
Output: Node with value 8

Input: 
List A: 2 -> 6 -> 4
List B: 1 -> 5
Output: nullptr
```

## Key Takeaways
- The algorithm has a time complexity of O(m + n), where m and n are the lengths of the two lists.
- The algorithm uses a constant amount of space, making it space-efficient.
- The algorithm assumes that the lists are non-circular and may have different lengths.