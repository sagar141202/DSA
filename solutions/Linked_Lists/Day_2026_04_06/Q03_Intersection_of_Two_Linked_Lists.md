# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the node where they intersect. The intersection node is the node where the two lists merge, i.e., the node with the same memory address in both lists. If there is no intersection, return nullptr. The lists may have different lengths and may not intersect at all. For example, given two linked lists a = [4,1,8,4,5] and b = [5,0,1,8,4,5], the intersection node is the node with value 8.

## Approach
We can solve this problem by using a two-pointer technique, where we traverse both lists and count their lengths. Then, we move the pointer of the longer list by the difference in lengths, so that both pointers are at the same distance from the end. Finally, we move both pointers one step at a time and check if they meet at a node.

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

        // move the pointer of the longer list
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

        // move both pointers and check for intersection
        while (tempA && tempB) {
            if (tempA == tempB) {
                return tempA;
            }
            tempA = tempA->next;
            tempB = tempB->next;
        }

        return nullptr;
    }
};
```

## Test Cases
```
Input: headA = [4,1,8,4,5], headB = [5,0,1,8,4,5]
Output: The node with value 8
```

## Key Takeaways
- The time complexity is O(m + n) where m and n are the lengths of the two linked lists.
- The space complexity is O(1) as we only use a constant amount of space to store the pointers and lengths.
- This solution assumes that the intersection node is the node with the same memory address in both lists.