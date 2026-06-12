# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list. Create a deep copy of the original list. The nodes in the new list should have the same values and random pointers as the nodes in the original list. The constraints are that we cannot modify the original list, and we must use extra space proportional to the number of nodes in the list. For example, given a list with nodes having values 1, 2, and 3, where the node with value 1 points to the node with value 3, and the node with value 2 points to the node with value 1, the copied list should also have the same structure and random pointers.

## Approach
We will use a hash map to store the mapping of the original nodes to the new nodes. Then, we will traverse the original list and create new nodes with the same values. We will also update the random pointers of the new nodes based on the hash map. This approach ensures that we create a deep copy of the original list with the same structure and random pointers.

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
        // Create a hash map to store the mapping of the original nodes to the new nodes
        unordered_map<Node*, Node*> map;

        // Traverse the original list and create new nodes with the same values
        Node* curr = head;
        while (curr) {
            map[curr] = new Node(curr->val);
            curr = curr->next;
        }

        // Update the next and random pointers of the new nodes
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
Input: [[1, 2], [2, 1]]
Output: [[1, 2], [2, 1]]
Input: [[1, null], [2, null], [3, null]]
Output: [[1, null], [2, null], [3, null]]
```

## Key Takeaways
- We use a hash map to store the mapping of the original nodes to the new nodes to avoid creating duplicate nodes.
- We traverse the original list twice: once to create new nodes with the same values, and once to update the next and random pointers of the new nodes.
- The time complexity is O(n), where n is the number of nodes in the list, because we traverse the list twice. The space complexity is also O(n) because we use a hash map to store the mapping of the original nodes to the new nodes.