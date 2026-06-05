# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the intersection point of the two lists. The intersection point is the node where the two lists merge. If there is no intersection, return null. The lists are non-circular and do not have any cycles. The intersection point can be anywhere in the lists, including the head. The lists have the following constraints: 0 <= list length <= 10^4, -10^5 <= node value <= 10^5.

## Approach
We can use a two-pointer technique to traverse both lists and find the intersection point. Calculate the lengths of both lists, then move the pointer of the longer list by the difference in lengths. Move both pointers one step at a time and check if the nodes are the same.

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
        // Calculate lengths of both lists
        int lenA = 0, lenB = 0;
        ListNode *tempA = headA, *tempB = headB;
        while (tempA) {
            lenA++;
            tempA = tempA->next;
        }
        while (tempB) {
            lenB++;
            tempB = tempB->next;
        }
        
        // Move the pointer of the longer list by the difference in lengths
        if (lenA > lenB) {
            for (int i = 0; i < lenA - lenB; i++) {
                headA = headA->next;
            }
        } else {
            for (int i = 0; i < lenB - lenA; i++) {
                headB = headB->next;
            }
        }
        
        // Move both pointers one step at a time and check if the nodes are the same
        while (headA && headB) {
            if (headA == headB) {
                return headA;
            }
            headA = headA->next;
            headB = headB->next;
        }
        
        return NULL;
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
Output: NULL
```

## Key Takeaways
- The two-pointer technique can be used to find the intersection point of two linked lists.
- Calculating the lengths of both lists is necessary to determine which list is longer.
- Moving the pointer of the longer list by the difference in lengths ensures that both pointers are at the same distance from the end of their respective lists.