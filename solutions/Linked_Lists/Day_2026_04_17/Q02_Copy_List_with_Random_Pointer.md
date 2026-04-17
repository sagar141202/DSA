# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. Create a deep copy of the original list. The list is represented as a linked list where each node is an instance of the Node class. The Node class has three attributes: val (the value of the node), next (the next node in the sequence), and random (a random node in the sequence). The task is to return the start of the copied linked list. The given constraints are: 0 <= n <= 1000, where n is the number of nodes in the list, and 10^4 <= Node.val <= 10^4. Node.random is null or is pointing to some node in the list.

## Approach
To solve this problem, we can use a hash map to store the nodes we have seen so far. We iterate over the original list, and for each node, we create a copy and store it in the hash map. Then, we update the next and random pointers of the copied nodes. This approach ensures that we avoid infinite loops and correctly copy the list with random pointers.

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

        // Create a hash map to store the nodes we have seen so far
        unordered_map<Node*, Node*> hash_map;

        // First pass: create a copy of each node and store it in the hash map
        Node* old_node = head;
        while (old_node) {
            hash_map[old_node] = new Node(old_node->val);
            old_node = old_node->next;
        }

        // Second pass: update the next and random pointers of the copied nodes
        old_node = head;
        while (old_node) {
            if (old_node->next) {
                hash_map[old_node]->next = hash_map[old_node->next];
            }
            if (old_node->random) {
                hash_map[old_node]->random = hash_map[old_node->random];
            }
            old_node = old_node->next;
        }

        return hash_map[head];
    }
};
```

## Test Cases
```
Input: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

## Key Takeaways
- Use a hash map to store the nodes we have seen so far to avoid infinite loops.
- Create a copy of each node and store it in the hash map in the first pass.
- Update the next and random pointers of the copied nodes in the second pass.