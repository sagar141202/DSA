# Copy List with Random Pointer

## Problem Statement
A linked list is given such that each node contains an integer value and a random pointer to any other node in the list. The task is to create a deep copy of the given list, ensuring that the random pointers in the copied list point to the correct nodes. The nodes in the list are defined by a Node class with two attributes: val (the value of the node) and random (the random pointer). The constraints are that the number of nodes in the list will be in the range [0, 1000], and the values of the nodes will be in the range [0, 10000]. An example of the problem is creating a copy of a list where the first node has a value of 1 and a random pointer to the second node, the second node has a value of 2 and a random pointer to the first node, and so on.

## Approach
The solution involves using a hash map to store the mapping between the original nodes and their corresponding copied nodes. This allows for efficient lookup and creation of the copied nodes. The algorithm iterates over the original list, creating a copy of each node and updating the random pointers accordingly. The approach ensures that each node is copied only once, reducing unnecessary computations.

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
        // Create a hash map to store the mapping between original nodes and their copies
        unordered_map<Node*, Node*> map;
        
        // Function to create a copy of a node
        function<Node*(Node*)> getClone = [&](Node* node) {
            if (!node) return nullptr;
            if (map.find(node) != map.end()) return map[node];
            Node* newNode = new Node(node->val);
            map[node] = newNode;
            return newNode;
        };

        // Create a copy of the list
        Node* old = head;
        Node* newHead = nullptr;
        Node* newTail = nullptr;
        while (old) {
            Node* newNode = getClone(old);
            if (!newHead) newHead = newNode;
            else newTail->next = newNode;
            newTail = newNode;
            old = old->next;
        }

        // Update the random pointers
        old = head;
        newTail = newHead;
        while (old) {
            newTail->random = getClone(old->random);
            old = old->next;
            newTail = newTail->next;
        }

        return newHead;
    }
};
```

## Test Cases
```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

## Key Takeaways
- Use a hash map to store the mapping between original nodes and their copies to avoid redundant computations.
- Create a copy of each node and update the random pointers in a separate pass to ensure correctness.
- Utilize a recursive function or a lambda function to simplify the process of creating a copy of a node.