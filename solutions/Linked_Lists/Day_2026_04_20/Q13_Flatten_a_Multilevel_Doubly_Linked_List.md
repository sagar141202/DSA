# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a previous pointer, and a child pointer. The child pointer points to the head of another linked list. Your task is to flatten this multilevel linked list into a single-level doubly linked list. The nodes should be connected in the order they appear in the original list, and the child pointers should be ignored. For example, given the following list: 
1---2---3---4---5---6
where 3 has a child node 7---8---9 and 8 has a child node 10---11, the flattened list should be 1---2---3---7---8---10---11---9---4---5---6.

## Approach
The approach is to perform a depth-first traversal of the linked list, and whenever we encounter a node with a child, we recursively flatten the child list and connect it to the current node. We keep track of the tail of the flattened list to connect the next nodes.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};

class Solution {
public:
    Node* flatten(Node* head) {
        if (!head) return head;
        
        Node* dummy = new Node(0);
        dummy->next = head;
        head->prev = dummy;
        
        Node* curr = dummy;
        
        while (curr) {
            if (curr->next) {
                curr->next->prev = curr;
            }
            if (curr->child) {
                Node* temp = curr->next;
                Node* tail = flatten(curr->child);
                curr->next = curr->child;
                curr->child->prev = curr;
                curr->child = nullptr;
                tail->next = temp;
                if (temp) {
                    temp->prev = tail;
                }
                curr = tail;
            } else {
                curr = curr->next;
            }
        }
        
        return dummy->next;
    }
};
```

## Test Cases
```
Input: 1---2---3---4---5---6
        |
        7---8---9
            |
            10---11
Output: 1---2---3---7---8---10---11---9---4---5---6
```

## Key Takeaways
- We use a recursive approach to flatten the child lists.
- We use a dummy node to simplify the code and handle the edge cases.
- The time complexity is O(N), where N is the total number of nodes in the linked list.