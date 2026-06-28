# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the node where they intersect. The intersection node is the node that is common to both linked lists. If there is no intersection, return null. The lists are non-cyclic and may have different lengths. For example, given two linked lists a = [4,1,8,4,5] and b = [5,0,1,8,4,5], the intersection node is the node with value 8.

## Approach
We can solve this problem by calculating the lengths of both linked lists and then moving the longer list forward by the difference in lengths. Then, we move both lists one step at a time and check if the nodes are the same. This approach ensures that we are comparing nodes at the same position in both lists.

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
        // Calculate the lengths of both linked lists
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

        // If there is no intersection, return null
        return NULL;
    }
};
```

## Test Cases
```
Input: a = [4,1,8,4,5], b = [5,0,1,8,4,5]
Output: The node with value 8
```

## Key Takeaways
- Calculate the lengths of both linked lists to determine the difference in lengths.
- Move the longer list forward by the difference in lengths to ensure both lists are at the same position.
- Move both lists one step at a time and check if the nodes are the same to find the intersection node.