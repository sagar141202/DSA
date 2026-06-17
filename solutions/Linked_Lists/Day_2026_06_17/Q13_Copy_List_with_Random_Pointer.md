# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an additional random pointer which could point to any node in the list, including itself. The task is to create a deep copy of the linked list, including the random pointers. The given linked list is defined by a Node class with an integer val and two pointers, next and random, pointing to the next node and a random node in the list respectively. The constraints are that 1 <= number of nodes <= 100 and 1 <= Node.val <= 100, and the nodes are numbered from 1 to N, where N is the number of nodes. The problem requires finding a way to efficiently create a copy of the linked list, ensuring that the original list remains unchanged.

## Approach
To solve this problem, we will use a hash map to store the mapping between the original nodes and their corresponding copied nodes. Then, we will iterate over the original list to create the copied nodes and update their next and random pointers accordingly. This approach allows us to efficiently handle the random pointers and create a deep copy of the linked list.

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
        // Create a hash map to store the mapping between the original nodes and their corresponding copied nodes
        unordered_map<Node*, Node*> hash;

        // Create the copied nodes and store them in the hash map
        Node* curr = head;
        while (curr) {
            hash[curr] = new Node(curr->val);
            curr = curr->next;
        }

        // Update the next and random pointers of the copied nodes
        curr = head;
        while (curr) {
            if (curr->next) {
                hash[curr]->next = hash[curr->next];
            }
            if (curr->random) {
                hash[curr]->random = hash[curr->random];
            }
            curr = curr->next;
        }

        // Return the head of the copied list
        return hash[head];
    }
};
```

## Test Cases
```
Input: 
Node 1 -> Node 2 -> Node 3
Node 1's random: Node 3
Node 2's random: Node 1
Node 3's random: Node 2

Output: 
Copied Node 1 -> Copied Node 2 -> Copied Node 3
Copied Node 1's random: Copied Node 3
Copied Node 2's random: Copied Node 1
Copied Node 3's random: Copied Node 2
```

## Key Takeaways
- We use a hash map to store the mapping between the original nodes and their corresponding copied nodes to efficiently handle the random pointers.
- We create the copied nodes and update their next and random pointers in two separate iterations to avoid any potential issues with the pointers.
- The time complexity of this solution is O(N), where N is the number of nodes in the linked list, as we iterate over the list twice. The space complexity is also O(N) due to the hash map.