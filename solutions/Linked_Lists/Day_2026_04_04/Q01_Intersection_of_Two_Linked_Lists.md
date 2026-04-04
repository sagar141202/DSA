# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the intersection point of the two lists. The intersection point is the node where the two lists merge. If the lists do not intersect, return NULL. The lists may have different lengths and may or may not intersect. For example, given two lists 4 -> 1 -> 8 -> 4 -> 5 and 5 -> 0 -> 1 -> 8 -> 4 -> 5, the intersection point is the node with value 8.

## Approach
The approach is to calculate the lengths of both lists and then move the longer list forward by the difference in lengths. Then, we move both lists one step at a time and check if the nodes are the same. If they are, we return the node as the intersection point.

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

        // Move the longer list forward by the difference in lengths
        tempA = headA;
        tempB = headB;
        if (lenA > lenB) {
            for (int i = 0; i < lenA - lenB; i++) {
                tempA = tempA->next;
            }
        } else {
            for (int i = 0; i < lenB - lenA; i++) {
                tempB = tempB->next;
            }
        }

        // Move both lists one step at a time and check if the nodes are the same
        while (tempA && tempB) {
            if (tempA == tempB) {
                return tempA;
            }
            tempA = tempA->next;
            tempB = tempB->next;
        }

        return NULL;
    }
};
```

## Test Cases
```
Input: headA = [4,1,8,4,5], headB = [5,0,1,8,4,5]
Output: The node with value 8
Input: headA = [0,9,1,2,4], headB = [3,2,4]
Output: The node with value 2
Input: headA = [2,6,4], headB = [1,5]
Output: NULL
```

## Key Takeaways
- We need to calculate the lengths of both lists to determine which list is longer.
- We move the longer list forward by the difference in lengths to align the lists.
- We then move both lists one step at a time and check if the nodes are the same to find the intersection point.