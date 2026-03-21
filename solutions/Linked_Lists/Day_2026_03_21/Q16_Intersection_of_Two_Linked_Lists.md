# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the intersection point of the two lists. The intersection point is the node where the two lists merge. If the lists do not intersect, return NULL. The lists are non-circular and do not contain cycles. Each node in the list has a unique value. The lists are defined as follows: 
- The first list is defined by the nodes with values a1, a2, ..., an.
- The second list is defined by the nodes with values b1, b2, ..., bm.
- ai and bj are the values of the ith and jth nodes in the first and second lists respectively.
- The intersection point is the node with value ak where k is the smallest index such that the node exists in both lists.

## Approach
We can solve this problem by calculating the lengths of both linked lists and then moving the pointer of the longer list by the difference in lengths. Then, we move both pointers one step at a time and check if they are the same node. If they are, we have found the intersection point.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
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
        while (tempA != NULL) {
            lenA++;
            tempA = tempA->next;
        }
        while (tempB != NULL) {
            lenB++;
            tempB = tempB->next;
        }

        // Move the pointer of the longer list by the difference in lengths
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

        // Move both pointers one step at a time and check if they are the same node
        while (tempA != NULL && tempB != NULL) {
            if (tempA == tempB) {
                return tempA;
            }
            tempA = tempA->next;
            tempB = tempB->next;
        }

        // If no intersection is found, return NULL
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
- We can solve this problem by calculating the lengths of both linked lists and then moving the pointer of the longer list by the difference in lengths.
- Then, we move both pointers one step at a time and check if they are the same node.
- If the lists do not intersect, we return NULL.