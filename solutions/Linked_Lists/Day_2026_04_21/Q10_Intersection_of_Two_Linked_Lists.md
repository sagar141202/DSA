# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the node where they intersect. The intersection is defined as the node where the two lists merge, or `nullptr` if they do not intersect. The lists may have different lengths, and the intersection node may not be the last node in either list. For example, given two linked lists `4 -> 1 -> 8 -> 4 -> 5` and `5 -> 0 -> 1 -> 8 -> 4 -> 5`, the intersection node is `8`. If the lists do not intersect, return `nullptr`.

## Approach
We can solve this problem by calculating the length of both linked lists, then moving the longer list forward by the difference in lengths. We then move both lists one step at a time and check for intersection. The algorithm uses the concept of two pointers and the properties of linked lists.

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

        // Move both lists one step at a time and check for intersection
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
Input: headA = [2,6,4], headB = [1,5]
Output: nullptr
```

## Key Takeaways
- The algorithm uses two pointers to traverse the linked lists.
- The time complexity is O(m + n), where m and n are the lengths of the two linked lists.
- The space complexity is O(1), as we only use a constant amount of space to store the pointers and variables.