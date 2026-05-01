# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the intersection point of the two lists. The intersection point is the node where the two lists merge. If there is no intersection, return nullptr. The lists are non-cyclic and may have different lengths. For example, given two lists 4 -> 1 -> 8 -> 4 -> 5 and 5 -> 0 -> 1 -> 8 -> 4 -> 5, the intersection point is the node with value 8.

## Approach
The approach is to calculate the difference in lengths of the two lists, then move the longer list forward by that difference. Then, move both lists one step at a time and check if the current nodes are the same. If they are, that node is the intersection point.

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
        // calculate the length of list A
        int lenA = 0;
        ListNode *tempA = headA;
        while (tempA) {
            lenA++;
            tempA = tempA->next;
        }
        
        // calculate the length of list B
        int lenB = 0;
        ListNode *tempB = headB;
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
        
        // move both lists one step at a time and check for intersection
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
List A: 4 -> 1 -> 8 -> 4 -> 5
List B: 5 -> 0 -> 1 -> 8 -> 4 -> 5
Output: The node with value 8

Input: 
List A: 2 -> 6 -> 4
List B: 1 -> 5
Output: nullptr
```

## Key Takeaways
- The time complexity of this solution is O(m + n), where m and n are the lengths of the two lists.
- The space complexity is O(1), as we only use a constant amount of space to store the lengths of the lists and the current nodes.
- This solution assumes that the lists are non-cyclic and may have different lengths.