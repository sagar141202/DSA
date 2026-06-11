# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the intersection point of the two lists. The intersection point is the node where the two lists merge, if they do. If the lists do not intersect, return null. The lists can have different lengths and the intersection point can be anywhere in the lists. For example, given two linked lists a = [4,1,8,4,5] and b = [5,0,1,8,4,5], the intersection point is the node with value 8.

## Approach
We can solve this problem by calculating the lengths of both lists and then moving the longer list forward by the difference in lengths. Then, we move both lists one step at a time and check if the nodes are the same. If they are, we return that node as the intersection point.

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
        
        // move longer list forward by difference in lengths
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
        
        // if no intersection is found
        return nullptr;
    }
};
```

## Test Cases
```
Input: 
List A: [4,1,8,4,5]
List B: [5,0,1,8,4,5]
Output: The node with value 8

Input: 
List A: [2,6,4]
List B: [1,5]
Output: null
```

## Key Takeaways
- We can solve this problem by moving the longer list forward by the difference in lengths, which allows us to compare nodes at the same position in both lists.
- We use a two-pointer technique to move both lists one step at a time and check for intersection.
- The time complexity is O(m + n) where m and n are the lengths of the two lists, and the space complexity is O(1) since we only use a constant amount of space.