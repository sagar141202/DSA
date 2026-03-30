# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. The task is to create a deep copy of the linked list, including the random pointers. Each node in the list has a unique value. The node structure is defined as follows: `struct Node { int val; Node *next; Node *random; };`. The constraints are: the number of nodes will not exceed 100, and the values of the nodes are between 1 and 10^5. The example is: given a list with nodes having values 7, 13, 11, and 10, and the next and random pointers as specified, create a deep copy of the list.

## Approach
To solve this problem, we can use a hashmap to store the mapping between the original nodes and their copies. Then we can iterate over the list to create the copies of the nodes and update the next and random pointers accordingly. This approach ensures that we create a deep copy of the linked list with the correct next and random pointers.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Definition for a Node.
struct Node {
    int val;
    Node *next;
    Node *random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        // Base case
        if (!head) return NULL;

        // Create a hashmap to store the mapping between the original nodes and their copies
        unordered_map<Node*, Node*> map;

        // Create copies of the nodes and store them in the hashmap
        Node* curr = head;
        while (curr) {
            map[curr] = new Node(curr->val);
            curr = curr->next;
        }

        // Update the next and random pointers of the copies
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
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

## Key Takeaways
- We need to use a hashmap to store the mapping between the original nodes and their copies to avoid creating duplicate copies.
- We should create the copies of the nodes first and then update the next and random pointers to avoid null pointer exceptions.
- The time complexity is O(N) where N is the number of nodes in the list, and the space complexity is also O(N) due to the hashmap.