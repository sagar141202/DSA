# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the intersection point of the two lists. The intersection point is the node where the two lists merge. If the lists do not intersect, return nullptr. The lists are non-circular and may have different lengths. For example, given two lists 4 -> 1 -> 8 -> 4 -> 5 and 5 -> 0 -> 1 -> 8 -> 4 -> 5, the intersection point is the node with value 8.

## Approach
The approach to solve this problem is to calculate the length of both linked lists, then move the longer list forward by the difference in lengths. After that, we can move both lists one step at a time and check if the current nodes are the same. If they are, we have found the intersection point.

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
        
        // Move both lists one step at a time and check if the current nodes are the same
        while (headA && headB) {
            if (headA == headB) {
                return headA;
            }
            headA = headA->next;
            headB = headB->next;
        }
        
        return nullptr;
    }
};
```

## Test Cases
```
Input: 
listA = [4,1,8,4,5]
listB = [5,0,1,8,4,5]
Output: 
The node with value 8
```

## Key Takeaways
- The time complexity of the solution is O(m + n), where m and n are the lengths of the two linked lists.
- The space complexity of the solution is O(1), as we only use a constant amount of space.
- The solution uses a two-pointer technique to find the intersection point of the two linked lists.