# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a previous pointer, and a child pointer. The child pointer points to the head of a child list, which is also a doubly linked list. The task is to flatten this multilevel doubly linked list into a single-level doubly linked list. The constraints are that the node values should be in the order they appear in the original list, and the child pointer should be ignored in the output list. For example, given the following list: 
1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6, where 3 has a child node 7 <-> 8 <-> 9, and 8 has a child node 10 <-> 11, the output list should be 1 <-> 2 <-> 3 <-> 7 <-> 8 <-> 10 <-> 11 <-> 9 <-> 4 <-> 5 <-> 6.

## Approach
We will use a recursive approach to flatten the multilevel doubly linked list. We will iterate through each node in the list, and if a node has a child, we will recursively flatten the child list and append it to the current node. We will then remove the child pointer from the current node.

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
        
        Node* curr = head;
        while (curr) {
            if (curr->child) {
                // Find the tail of the child list
                Node* childTail = curr->child;
                while (childTail->next) childTail = childTail->next;
                
                // Find the next node in the main list
                Node* nextNode = curr->next;
                
                // Connect the child list to the main list
                childTail->next = nextNode;
                if (nextNode) nextNode->prev = childTail;
                curr->next = curr->child;
                curr->child->prev = curr;
                curr->child = nullptr;
            }
            curr = curr->next;
        }
        return head;
    }
};
```

## Test Cases
```
Input: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6, where 3 has a child node 7 <-> 8 <-> 9, and 8 has a child node 10 <-> 11
Output: 1 <-> 2 <-> 3 <-> 7 <-> 8 <-> 10 <-> 11 <-> 9 <-> 4 <-> 5 <-> 6
```

## Key Takeaways
- We use a recursive approach to flatten the multilevel doubly linked list, but in this case, we can also solve it iteratively.
- We iterate through each node in the list and check if it has a child. If it does, we recursively flatten the child list and append it to the current node.
- We use a while loop to traverse the list, and we update the next and previous pointers of the nodes accordingly.