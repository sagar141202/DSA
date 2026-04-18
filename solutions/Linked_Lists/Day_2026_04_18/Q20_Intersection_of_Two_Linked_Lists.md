# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find their intersection node. The intersection node is the node where the two linked lists merge. If there is no intersection, return null. The lists are non-empty and do not contain cycles. For example, given two linked lists `4 -> 1 -> 8 -> 4 -> 5` and `5 -> 0 -> 1 -> 8 -> 4 -> 5`, the intersection node is `8`. If the two linked lists have no intersection, return `null`.

## Approach
The algorithm involves calculating the lengths of both linked lists, then moving the longer list's pointer by the difference in lengths. After that, move both pointers one step at a time and check for intersection.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        // Calculate lengths of both linked lists
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

        // Move longer list's pointer by the difference in lengths
        if (lenA > lenB) {
            for (int i = 0; i < lenA - lenB; i++) {
                headA = headA->next;
            }
        } else {
            for (int i = 0; i < lenB - lenA; i++) {
                headB = headB->next;
            }
        }

        // Move both pointers one step at a time and check for intersection
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
Output: 8

Input: 
List A: 2 -> 6 -> 4
List B: 1 -> 5
Output: null
```

## Key Takeaways
- We can find the intersection of two linked lists by calculating their lengths and moving the longer list's pointer by the difference in lengths.
- We can then move both pointers one step at a time and check for intersection.
- This approach has a time complexity of O(m + n), where m and n are the lengths of the two linked lists.