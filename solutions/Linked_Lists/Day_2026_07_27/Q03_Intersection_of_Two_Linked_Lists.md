# Intersection of Two Linked Lists

## Problem Statement
Given two linked lists, find the intersection point of the two lists if it exists. The intersection point is where the two lists merge into a single list. The lists are non-cyclic and each node has a unique value. If there is no intersection, return nullptr. For example, given two lists 4 -> 1 -> 8 -> 4 -> 5 and 5 -> 6 -> 1 -> 8 -> 4 -> 5, the intersection point is the node with value 8.

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
        // Calculate lengths of both lists
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
        
        // If no intersection is found, return nullptr
        return nullptr;
    }
};
```

## Test Cases
```
Input: 
List A: 4 -> 1 -> 8 -> 4 -> 5
List B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
Output: Node with value 8

Input: 
List A: 2 -> 6 -> 4
List B: 1 -> 5
Output: nullptr
```

## Key Takeaways
- We can solve this problem by calculating the lengths of both lists and then moving the longer list forward by the difference in lengths.
- We move both lists one step at a time and check if the nodes are the same to find the intersection point.
- The time complexity of this solution is O(m + n), where m and n are the lengths of the two lists.