# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find their intersection point. The intersection point is where the two linked lists merge into a single linked list. If there is no intersection, return null. The linked lists are non-circular and may have different lengths. For example, given two linked lists `4 -> 1 -> 8 -> 4 -> 5` and `5 -> 0 -> 1 -> 8 -> 4 -> 5`, the intersection point is the node with value `8`.

## Approach
We can solve this problem by calculating the lengths of both linked lists and then moving the longer list forward by the difference in lengths. Then, we can move both lists one step at a time and check if the nodes are the same.

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
        // calculate lengths of both linked lists
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
        
        // move the longer list forward by the difference in lengths
        if (lenA > lenB) {
            for (int i = 0; i < lenA - lenB; i++) {
                headA = headA->next;
            }
        } else {
            for (int i = 0; i < lenB - lenA; i++) {
                headB = headB->next;
            }
        }
        
        // move both lists one step at a time and check if the nodes are the same
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
listA = [4,1,8,4,5]
listB = [5,0,1,8,4,5]
Output: The node with value 8

Input: 
listA = [1,9,1,2,4]
listB = [3,2,4]
Output: The node with value 2
```

## Key Takeaways
- Calculate the lengths of both linked lists to determine which list is longer.
- Move the longer list forward by the difference in lengths to align the lists.
- Move both lists one step at a time and check if the nodes are the same to find the intersection point.