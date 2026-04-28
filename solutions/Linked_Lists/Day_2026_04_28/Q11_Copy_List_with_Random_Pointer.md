# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. The task is to create a deep copy of the original list. The given list is defined by a Node class, where each node has a value, a next pointer, and a random pointer. The constraints are that 1 <= Number of Nodes <= 100 and 1 <= Node.val <= 100. The node's next pointer and random pointer can be null. An example would be a list where the first node has a value of 7, the second node has a value of 13, the third node has a value of 11, and the fourth node has a value of 10. The first node's random pointer points to the third node, the second node's random pointer points to the first node, and the rest of the nodes do not have random pointers.

## Approach
We will use a hash map to store the nodes of the original list as keys and the corresponding nodes of the copied list as values. This allows us to handle the random pointers efficiently by simply looking up the corresponding node in the hash map. We will then create a new node for each node in the original list and update its next and random pointers.

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

        Node* curr = head;
        unordered_map<Node*, Node*> map;

        // Create a copy of each node and store it in the map
        while (curr) {
            map[curr] = new Node(curr->val);
            curr = curr->next;
        }

        curr = head;

        // Update the next and random pointers of the copied nodes
        while (curr) {
            if (curr->next) {
                map[curr]->next = map[curr->next];
            }
            if (curr->random) {
                map[curr]->random = map[curr->random];
            }
            curr = curr->next;
        }

        return map[head];
    }
};
```

## Test Cases
```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

## Key Takeaways
- Use a hash map to store the nodes of the original list and their corresponding copied nodes.
- Create a copy of each node and update its next and random pointers using the hash map.
- The time complexity is linear because we visit each node twice, once to create the copy and once to update the pointers.