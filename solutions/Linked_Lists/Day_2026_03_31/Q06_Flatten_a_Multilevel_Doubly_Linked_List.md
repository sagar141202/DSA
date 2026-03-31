# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a previous pointer, and a child pointer. The child pointer points to the head of another doubly linked list, which is also a multilevel doubly linked list. The task is to flatten the multilevel doubly linked list into a single-level doubly linked list. The nodes in the flattened list should be in the order of their appearance in the original list, and the next and previous pointers should be updated accordingly. For example, given the following multilevel doubly linked list:
```
 1---2---3---4---5---6
          |
          7---8---9
              |
              10---11
```
The flattened list should be:
```
1---2---3---7---8---10---11---4---5---6
```
The constraints are:
- The number of nodes in the list is between 1 and 1000.
- The value of each node is between 1 and 1000.

## Approach
We can solve this problem by iterating through the list and appending the child list to the current node when we encounter a node with a child. We will use a recursive approach to flatten the child lists.

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
        flattenHelper(dummy, head);
        Node* newHead = dummy->next;
        newHead->prev = nullptr;
        delete dummy;
        return newHead;
    }
    
    void flattenHelper(Node* prev, Node* curr) {
        if (!curr) return;
        curr->prev = prev;
        prev->next = curr;
        Node* temp = curr->next;
        if (curr->child) {
            flattenHelper(curr, curr->child);
            curr->child = nullptr;
            Node* tail = curr;
            while (tail->next) {
                tail = tail->next;
            }
            tail->next = temp;
            if (temp) {
                temp->prev = tail;
            }
        }
        flattenHelper(curr, temp);
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
Output: 1---2---3---7---8---10---11---4---5---6
```

## Key Takeaways
- Use a recursive approach to flatten the child lists.
- Update the next and previous pointers of the nodes in the flattened list.
- Use a dummy node to simplify the code and avoid edge cases.