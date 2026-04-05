# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a prev pointer, and a child pointer. The child pointer points to the head of a new linked list, which can also have a child pointer, and so on. The task is to flatten this multilevel linked list into a single-level doubly linked list. The constraints are that the nodes should be visited in the order of their values, and if two nodes have the same value, the node that appears first in the original linked list should appear first in the flattened linked list. For example, given the following multilevel linked list: 
1 -> 2 -> 3 -> 4 -> 5 -> 6, where 3 has a child 7 -> 8 -> 9, and 8 has a child 10 -> 11, the flattened linked list should be 1 -> 2 -> 3 -> 7 -> 8 -> 10 -> 11 -> 9 -> 4 -> 5 -> 6.

## Approach
To solve this problem, we can use a recursive approach to traverse the linked list and its children. We will define a function that takes a node as an argument and returns the last node in the flattened linked list. If a node has a child, we will recursively call the function on the child and then connect the last node of the child's linked list to the next node in the original linked list.

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
        Node* dummy = new Node();
        dummy->next = head;
        flattenHelper(dummy);
        Node* newHead = dummy->next;
        delete dummy;
        return newHead;
    }
    
    void flattenHelper(Node* node) {
        Node* curr = node;
        while (curr) {
            if (curr->child) {
                Node* temp = curr->next;
                Node* childTail = curr->child;
                while (childTail->next) {
                    childTail = childTail->next;
                }
                childTail->next = temp;
                if (temp) temp->prev = childTail;
                curr->next = curr->child;
                curr->child->prev = curr;
                curr->child = nullptr;
                curr = childTail;
            }
            curr = curr->next;
        }
    }
};
```

## Test Cases
```
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6, where 3 has a child 7 -> 8 -> 9, and 8 has a child 10 -> 11
Output: 1 -> 2 -> 3 -> 7 -> 8 -> 10 -> 11 -> 9 -> 4 -> 5 -> 6
```

## Key Takeaways
- To flatten a multilevel linked list, we can use a recursive approach to traverse the linked list and its children.
- We need to keep track of the last node in the flattened linked list to connect it to the next node in the original linked list.
- The time complexity is O(N), where N is the total number of nodes in the linked list and its children.