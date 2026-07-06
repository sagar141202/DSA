# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. The task is to create a deep copy of the given linked list, ensuring that the original and copied lists are completely independent of each other. Each node in the list has a unique value. The constraint is that the input linked list can be empty.

## Approach
To solve this problem, we will use a hash map to store the mapping between the original nodes and their corresponding copied nodes. Then, we will traverse the original list to create the copied list and update the next and random pointers accordingly.

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
    Node(int x) : val(x), next(NULL), random(NULL) {}
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        // Create a hash map to store the mapping between original nodes and copied nodes
        unordered_map<Node*, Node*> map;
        
        // Traverse the original list to create the copied nodes and store them in the hash map
        Node* curr = head;
        while (curr) {
            map[curr] = new Node(curr->val);
            curr = curr->next;
        }
        
        // Traverse the original list again to update the next and random pointers of the copied nodes
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
- We use a hash map to store the mapping between original nodes and copied nodes to avoid creating duplicate copied nodes.
- We traverse the original list twice: first to create the copied nodes and store them in the hash map, and second to update the next and random pointers of the copied nodes.
- The time complexity is O(N), where N is the number of nodes in the original list, because we traverse the list twice. The space complexity is also O(N) because we create a hash map to store the mapping between original nodes and copied nodes.