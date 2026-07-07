# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the intersection point of the two lists if it exists, and return the intersection node. If there is no intersection, return null. The lists do not have cycles, and the intersection node is defined by reference, not value. For example, consider two linked lists A = 4 -> 1 -> 8 -> 4 -> 5 and B = 5 -> 0 -> 1 -> 8 -> 4 -> 5, the intersection point is the node with value 8.

## Approach
We can solve this problem by calculating the lengths of both linked lists and then moving the longer list forward by the difference in lengths. Then, we move both lists one step at a time and check if the nodes are the same. If they are, we return the intersection node.

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
        // Calculate lengths of both linked lists
        int lenA = 0, lenB = 0;
        ListNode *tempA = headA, *tempB = headB;
        while (tempA != NULL) {
            lenA++;
            tempA = tempA->next;
        }
        while (tempB != NULL) {
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
        while (tempA != NULL && tempB != NULL) {
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
Input: headA = [2,6,4], headB = [1,5]
Output: null
```

## Key Takeaways
- The time complexity of this solution is O(m + n), where m and n are the lengths of the two linked lists.
- The space complexity of this solution is O(1), as we only use a constant amount of space to store the lengths of the lists and the current nodes.
- This solution assumes that the intersection node is defined by reference, not value.