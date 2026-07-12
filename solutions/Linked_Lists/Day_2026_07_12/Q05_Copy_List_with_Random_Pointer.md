# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. The task is to create a deep copy of the original list. The deep copy should include all the nodes with their respective next and random pointers. It is guaranteed that the input linked list has at least one node.

## Approach
Create a hash map to store the mapping between the original nodes and their copies, then iterate over the list to copy the next and random pointers. The algorithm ensures that each node is copied only once.

## Complexity
- Time: O(N)
- Space: O(N)

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
        unordered_map<Node*, Node*> map;
        Node* curr = head;
        while (curr) {
            map[curr] = new Node(curr->val);
            curr = curr->next;
        }

        // Copy the next and random pointers
        curr = head;
        while (curr) {
            if (curr->next) map[curr]->next = map[curr->next];
            if (curr->random) map[curr]->random = map[curr->random];
            curr = curr->next;
        }

        return map[head];
    }
};
```

## Test Cases
```
Input: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

## Key Takeaways
- Use a hash map to store the mapping between the original nodes and their copies to avoid duplicate copying.
- Copy the next and random pointers separately to ensure that each node is correctly linked.
- The algorithm has a time complexity of O(N) and a space complexity of O(N), where N is the number of nodes in the list.