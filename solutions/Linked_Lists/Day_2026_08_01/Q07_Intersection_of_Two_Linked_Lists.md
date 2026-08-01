# Intersection of Two Linked Lists

## Problem Statement
Given two non-empty linked lists, find their intersection node. The intersection node is the node where the two linked lists meet. If there is no intersection, return null. Note that the intersection node is the same node in both linked lists, not just a node with the same value. The lists are non-empty and may have different lengths. For example, given two linked lists a = [4,1,8,4,5] and b = [5,0,1,8,4,5], their intersection is the node with value 8, which is the node with value 8 in both lists.

## Approach
We can solve this problem by calculating the length of both linked lists and then moving the longer list forward by the difference in lengths. Then, we move both lists one step at a time and check if the nodes are the same. If they are, we return the node as the intersection. If we reach the end of either list without finding an intersection, we return null.

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

        // If we reach the end of either list without finding an intersection, return null
        return nullptr;
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
listA = [1,2,3]
listB = [4,5,6]
Output: null
```

## Key Takeaways
- Calculate the lengths of both linked lists to determine which list is longer.
- Move the longer list forward by the difference in lengths to align the lists.
- Move both lists one step at a time and check if the nodes are the same to find the intersection.