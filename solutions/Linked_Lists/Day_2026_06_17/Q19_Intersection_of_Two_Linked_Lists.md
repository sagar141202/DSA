# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the node where they intersect. The intersection is defined as the node where the two lists merge and have the same nodes after that point. If there is no intersection, return null. The lists do not necessarily have to be the same length, and the intersection can occur at any node. For example, given two linked lists: 4 -> 1 -> 8 -> 4 -> 5 and 5 -> 0 -> 1 -> 8 -> 4 -> 5, the intersection occurs at node 8.

## Approach
We can solve this problem by calculating the length of both linked lists, then moving the longer list forward by the difference in lengths. After that, we can move both lists one step at a time and check if the nodes are the same. If they are, we have found the intersection point. If not, we continue moving until we reach the end of either list.

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
        // Calculate the length of both linked lists
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
        if (lenA > lenB) {
            for (int i = 0; i < lenA - lenB; i++) {
                headA = headA->next;
            }
        } else {
            for (int i = 0; i < lenB - lenA; i++) {
                headB = headB->next;
            }
        }
        
        // Move both lists one step at a time and check if the nodes are the same
        while (headA && headB) {
            if (headA == headB) {
                return headA;
            }
            headA = headA->next;
            headB = headB->next;
        }
        
        // If no intersection is found, return null
        return NULL;
    }
};
```

## Test Cases
```
Input: headA = [4,1,8,4,5], headB = [5,0,1,8,4,5]
Output: The node with value 8
Input: headA = [2,6,4], headB = [1,5]
Output: null
```

## Key Takeaways
- To find the intersection of two linked lists, we need to calculate the length of both lists and move the longer list forward by the difference in lengths.
- We then move both lists one step at a time and check if the nodes are the same to find the intersection point.
- If no intersection is found after moving both lists, we return null to indicate that there is no intersection.