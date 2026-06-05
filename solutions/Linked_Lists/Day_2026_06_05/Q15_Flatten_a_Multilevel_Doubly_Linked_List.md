# Flatten a Multilevel Doubly Linked List

## Problem Statement
You are given a multilevel doubly linked list, where each node has a value, a next pointer, a prev pointer, and a child pointer. The child pointer points to the head of a new linked list, which can also have a child pointer, and so on. The task is to flatten this multilevel doubly linked list into a single-level doubly linked list, where all nodes are connected through their next and prev pointers. The nodes should be connected in the order they appear in the original list, with the child list nodes appearing after their parent node. For example, given the list 1 -> 2 -> 3 -> 4 -> 5 -> 6, where 3 has a child list 7 -> 8 -> 9, and 8 has a child list 10 -> 11, the flattened list should be 1 -> 2 -> 3 -> 7 -> 8 -> 10 -> 11 -> 9 -> 4 -> 5 -> 6.

## Approach
The algorithm involves traversing the linked list and appending the child list to the main list whenever a child pointer is encountered. This is done recursively to handle multilevel lists. The next and prev pointers of the nodes are updated accordingly to maintain the correct order.

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
        // Base case: if the list is empty, return NULL
        if (!head) return NULL;

        // Initialize a pointer to the current node
        Node* current = head;

        // Traverse the list until the end is reached
        while (current) {
            // If the current node has a child, flatten the child list and append it to the main list
            if (current->child) {
                // Find the last node of the child list
                Node* lastChild = current->child;
                while (lastChild->next) lastChild = lastChild->next;

                // Update the next and prev pointers of the current node and the last child node
                lastChild->next = current->next;
                if (current->next) current->next->prev = lastChild;
                current->next = current->child;
                current->child->prev = current;
                current->child = NULL;
            }

            // Move to the next node
            current = current->next;
        }

        // Return the head of the flattened list
        return head;
    }
};
```

## Test Cases
```
Input: 
1 -> 2 -> 3 -> 4 -> 5 -> 6
where 3 has a child list 7 -> 8 -> 9
and 8 has a child list 10 -> 11

Output: 
1 -> 2 -> 3 -> 7 -> 8 -> 10 -> 11 -> 9 -> 4 -> 5 -> 6
```

## Key Takeaways
- The key to solving this problem is to understand how to traverse and update the pointers of a multilevel doubly linked list.
- The use of recursion can simplify the solution by handling the child lists in a separate function call.
- It's essential to update the next and prev pointers correctly to maintain the correct order in the flattened list.