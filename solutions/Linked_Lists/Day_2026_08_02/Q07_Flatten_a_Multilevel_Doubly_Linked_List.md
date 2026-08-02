# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a prev pointer, and a child pointer. The task is to flatten the list so that all nodes are at the same level, and the next pointer of each node points to the next node in the flattened list. The child pointer of each node should be set to NULL. The list is guaranteed to be non-cyclic. For example, given the following multilevel doubly linked list: 
1---2---3---4---5---6
        |
        7---8---9
            |
            10
The flattened list should be: 
1---2---3---7---8---10---4---5---6

## Approach
We will use a recursive approach to solve this problem. Starting from the head of the list, we will recursively flatten the child list and insert it into the main list. We will keep track of the tail of the flattened list to ensure that the next pointer of each node points to the next node in the flattened list.

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
        
        Node* current = head;
        while (current) {
            if (current->child) {
                Node* temp = current->next;
                Node* child = current->child;
                current->next = child;
                child->prev = current;
                current->child = NULL;
                
                Node* tail = getTail(child);
                tail->next = temp;
                if (temp) temp->prev = tail;
            }
            current = current->next;
        }
        
        Node* newHead = dummy->next;
        newHead->prev = NULL;
        delete dummy;
        return newHead;
    }
    
    Node* getTail(Node* head) {
        Node* current = head;
        while (current->next) {
            current = current->next;
        }
        return current;
    }
};
```

## Test Cases
```
Input: 
1---2---3---4---5---6
        |
        7---8---9
            |
            10
Output: 
1---2---3---7---8---10---4---5---6
```

## Key Takeaways
- To solve this problem, we need to use a recursive approach to flatten the child list and insert it into the main list.
- We need to keep track of the tail of the flattened list to ensure that the next pointer of each node points to the next node in the flattened list.
- The time complexity of this solution is O(N), where N is the number of nodes in the list.