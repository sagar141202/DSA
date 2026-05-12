# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an integer value and two pointers, `next` and `random`, which point to the next node and a random node in the list respectively. The task is to create a deep copy of the given linked list, i.e., to create a new linked list where each node has the same value and points to the corresponding nodes in the new list. The given list may contain cycles and the nodes may point to each other in any order.

## Approach
The algorithm involves traversing the list and creating a new node for each node in the original list. It uses a hash map to store the mapping between the original nodes and their copies. This allows us to efficiently find the copy of a node when we need to set the `next` or `random` pointer of a node.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return NULL;
        
        // Create a hash map to store the mapping between the original nodes and their copies
        unordered_map<Node*, Node*> nodeMap;
        
        // Traverse the list and create a new node for each node in the original list
        Node* orig = head;
        Node* newHead = new Node(orig->val);
        Node* newCurr = newHead;
        nodeMap[orig] = newCurr;
        
        orig = orig->next;
        while (orig) {
            newCurr->next = new Node(orig->val);
            nodeMap[orig] = newCurr->next;
            newCurr = newCurr->next;
            orig = orig->next;
        }
        
        // Set the random pointers of the new nodes
        orig = head;
        newCurr = newHead;
        while (orig) {
            if (orig->random) {
                newCurr->random = nodeMap[orig->random];
            }
            orig = orig->next;
            newCurr = newCurr->next;
        }
        
        return newHead;
    }
};

```

## Test Cases
```
Input: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

## Key Takeaways
- We use a hash map to store the mapping between the original nodes and their copies to efficiently find the copy of a node.
- We traverse the list twice, first to create the new nodes and then to set the random pointers.
- The time complexity is O(n) and the space complexity is O(n), where n is the number of nodes in the list.