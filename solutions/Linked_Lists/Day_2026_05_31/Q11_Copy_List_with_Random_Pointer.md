# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an integer value and a random pointer to another node in the list. The task is to create a deep copy of the given linked list, ensuring that the random pointers in the copied list point to the corresponding nodes in the copied list. The given linked list is represented as a sequence of nodes, where each node has a val and a random pointer. The constraints are that the number of nodes in the list will not exceed 100, and the values of the nodes will be between 1 and 10^4.

## Approach
To solve this problem, we can use a hash map to store the mapping between the original nodes and their corresponding copied nodes. Then, we can iterate through the original list, creating a new node for each node in the original list and updating the next and random pointers accordingly.

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
        // Create a hash map to store the mapping between original nodes and copied nodes
        unordered_map<Node*, Node*> map;
        
        // Create a new node for each node in the original list
        Node* curr = head;
        while (curr) {
            map[curr] = new Node(curr->val);
            curr = curr->next;
        }
        
        // Update the next and random pointers for each node in the copied list
        curr = head;
        while (curr) {
            if (curr->next) {
                map[curr]->next = map[curr->next];
            }
            if (curr->random) {
                map[curr]->random = map[curr->random];
            }
            curr = curr->next;
        }
        
        // Return the head of the copied list
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
- Use a hash map to store the mapping between original nodes and copied nodes to efficiently update the next and random pointers.
- Create a new node for each node in the original list to ensure a deep copy of the list.
- Update the next and random pointers for each node in the copied list by looking up the corresponding nodes in the hash map.