# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the intersection point of the two lists if it exists. The intersection point is the node where the two lists merge. If no intersection exists, return null. The lists are non-circular and may have different lengths. For example, given two linked lists `4 -> 1 -> 8 -> 4 -> 5` and `5 -> 0 -> 1 -> 8 -> 4 -> 5`, the intersection point is the node with value `8`.

## Approach
The algorithm uses a two-pointer technique to traverse both lists and find the intersection point. It calculates the lengths of both lists, then moves the pointer of the longer list forward by the difference in lengths. Finally, it moves both pointers one step at a time and checks for intersection.

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

        // Move pointer of longer list forward by difference in lengths
        if (lenA > lenB) {
            for (int i = 0; i < lenA - lenB; i++) {
                headA = headA->next;
            }
        } else {
            for (int i = 0; i < lenB - lenA; i++) {
                headB = headB->next;
            }
        }

        // Move both pointers one step at a time and check for intersection
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
- Use a two-pointer technique to traverse both lists and find the intersection point.
- Calculate the lengths of both lists to determine which list is longer.
- Move the pointer of the longer list forward by the difference in lengths to ensure both pointers are at the same distance from the end of their respective lists.