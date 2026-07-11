# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the intersection point of the two lists. The intersection point is the node where the two lists merge. If there is no intersection, return null. The lists are non-cyclic and may have different lengths. For example, given two lists: 4 -> 1 -> 8 -> 4 -> 5 and 5 -> 0 -> 1 -> 8 -> 4 -> 5, the intersection point is the node with value 8.

## Approach
The approach to solve this problem is to calculate the lengths of both linked lists, then move the longer list forward by the difference in lengths. After that, move both lists one step at a time and check if the current nodes are the same. If they are, return the current node as the intersection point.

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
        // calculate lengths of both lists
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
        
        // move longer list forward
        if (lenA > lenB) {
            for (int i = 0; i < lenA - lenB; i++) {
                headA = headA->next;
            }
        } else {
            for (int i = 0; i < lenB - lenA; i++) {
                headB = headB->next;
            }
        }
        
        // find intersection point
        while (headA && headB) {
            if (headA == headB) return headA;
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
Output: 8

Input: 
List A: 2 -> 6 -> 4
List B: 1 -> 5
Output: NULL
```

## Key Takeaways
- We need to calculate the lengths of both linked lists to determine which list is longer.
- We move the longer list forward by the difference in lengths to ensure both lists have the same remaining length.
- We then move both lists one step at a time and check if the current nodes are the same to find the intersection point.