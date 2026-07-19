# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the intersection point of the two lists. The intersection point is the node where the two lists merge. If there is no intersection, return NULL. The lists are non-cyclic and each node has a unique value. For example, given two lists 4 -> 1 -> 8 -> 4 -> 5 and 5 -> 0 -> 1 -> 8 -> 4 -> 5, the intersection point is the node with value 8.

## Approach
We can solve this problem by calculating the lengths of both lists and then moving the pointer of the longer list ahead by the difference in lengths. Then, we move both pointers one step at a time and check if they meet at any point. If they do, that point is the intersection point.

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

        // Move the pointer of the longer list ahead
        if (lenA > lenB) {
            for (int i = 0; i < lenA - lenB; i++) {
                headA = headA->next;
            }
        } else {
            for (int i = 0; i < lenB - lenA; i++) {
                headB = headB->next;
            }
        }

        // Move both pointers one step at a time
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
- To find the intersection point of two linked lists, we need to calculate the lengths of both lists and move the pointer of the longer list ahead by the difference in lengths.
- We then move both pointers one step at a time and check if they meet at any point.
- The time complexity of this solution is O(m + n), where m and n are the lengths of the two lists.