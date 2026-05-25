# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an integer value and a random pointer to another node in the list. The task is to create a deep copy of the original list. The deep copy should have the same structure as the original list, i.e., the random pointer of each node in the copied list should point to the corresponding node in the copied list. The given linked list is represented as a Node class with two attributes: val (an integer representing the value of the node) and next (a pointer to the next node in the list), and random (a pointer to a random node in the list). The constraints are that the number of nodes in the list will not exceed 100, and the values of the nodes will be in the range [0, 100]. For example, if the original list is 1 -> 2 -> 3 with random pointers 1 -> 3, 2 -> 1, 3 -> 2, the copied list should also have the same structure and random pointers.

## Approach
Create a hash map to store the mapping between the original nodes and their copies. Traverse the original list to create a copy of each node and store the mapping in the hash map. Then, traverse the original list again to set the next and random pointers of the copied nodes. This approach ensures that the copied list has the same structure as the original list.

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
        unordered_map<Node*, Node*> map;
        Node* curr = head;
        while (curr) {
            map[curr] = new Node(curr->val);
            curr = curr->next;
        }

        // Set the next and random pointers of the copied nodes
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
Input: head = [1,2,3] with random pointers [3,1,2]
Output: head = [1,2,3] with random pointers [3,1,2]
```

## Key Takeaways
- Use a hash map to store the mapping between the original nodes and their copies to efficiently create the copied list.
- Traverse the original list twice: once to create the copies of the nodes and store the mapping, and again to set the next and random pointers of the copied nodes.