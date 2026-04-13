# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a prev pointer, and a child pointer. The task is to flatten this multilevel doubly linked list into a single-level doubly linked list. The child pointer of a node can point to another node in the list, and we need to insert all nodes that are reachable from a node via its child pointer after that node in the flattened list. The given list is a doubly linked list, so we need to update the next and prev pointers of the nodes accordingly. For example, if we have a list 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6, where node 3 has a child node 7, node 7 has a child node 8, node 8 has a child node 9, and node 9 has a child node 10, then the flattened list should be 1 <-> 2 <-> 3 <-> 7 <-> 8 <-> 9 <-> 10 <-> 4 <-> 5 <-> 6.

## Approach
We will use a recursive approach to solve this problem. We will define a function that takes a node as input and returns the last node in the flattened list starting from the given node. We will then use this function to flatten the entire list.

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
        
        while (curr->next) {
            if (curr->next->child) {
                Node* child = curr->next->child;
                Node* temp = curr->next->next;
                
                curr->next->next = child;
                child->prev = curr->next;
                
                Node* tail = getTail(child);
                tail->next = temp;
                if (temp) temp->prev = tail;
                
                curr->next->child = nullptr;
            }
            curr = curr->next;
        }
        
        dummy->next->prev = nullptr;
        return dummy->next;
    }
    
    Node* getTail(Node* head) {
        Node* curr = head;
        while (curr->next) curr = curr->next;
        return curr;
    }
};
```

## Test Cases
```
Input: 
1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6
where node 3 has a child node 7,
node 7 has a child node 8,
node 8 has a child node 9,
and node 9 has a child node 10.
Output: 
1 <-> 2 <-> 3 <-> 7 <-> 8 <-> 9 <-> 10 <-> 4 <-> 5 <-> 6
```

## Key Takeaways
- The problem can be solved using a recursive approach.
- We need to define a function that takes a node as input and returns the last node in the flattened list starting from the given node.
- We need to update the next and prev pointers of the nodes accordingly to maintain the doubly linked list structure.