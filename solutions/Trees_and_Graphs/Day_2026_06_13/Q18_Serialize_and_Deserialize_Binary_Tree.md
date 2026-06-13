# Serialize and Deserialize Binary Tree

## Problem Statement
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment. Deserialization is the reverse process, where the sequence of bits is converted back into a data structure or object. Given the root of a binary tree, serialize the tree into a string, and then deserialize the string back into the original tree structure. The serialization of a binary tree is a string representation of the binary tree where each node is represented by its value followed by a comma (except the last node), and null nodes are represented by 'X'. For example, the serialization of the binary tree below is "1,2,X,X,3,X,X". 
        1
       / \
      2   3
     / \
    X   X
The constraints are:
- The number of nodes in the tree is in the range [0, 10^4].
- -10^4 <= Node.val <= 10^4.

## Approach
We can solve this problem using a recursive depth-first search (DFS) approach to serialize the tree and a recursive DFS approach to deserialize the string. The serialization process involves traversing the tree and appending the node values and 'X' for null nodes to the result string. The deserialization process involves recursively creating nodes and assigning their values based on the serialized string.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        ostringstream oss;
        serializeHelper(root, oss);
        return oss.str();
    }

    void serializeHelper(TreeNode* node, ostringstream& oss) {
        if (node == NULL) {
            oss << "X,";
            return;
        }
        oss << node->val << ",";
        serializeHelper(node->left, oss);
        serializeHelper(node->right, oss);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream iss(data);
        return deserializeHelper(iss);
    }

    TreeNode* deserializeHelper(istringstream& iss) {
        string val;
        getline(iss, val, ',');
        if (val == "X") {
            return NULL;
        }
        TreeNode* node = new TreeNode(stoi(val));
        node->left = deserializeHelper(iss);
        node->right = deserializeHelper(iss);
        return node;
    }
};
```

## Test Cases
```
Input: root = [1,2,3,null,null,4,5]
Output: "1,2,X,X,3,4,X,X,5,X,X"
```

## Key Takeaways
- Use recursive DFS for both serialization and deserialization.
- Handle null nodes by using a sentinel value like 'X'.
- Use string streams for efficient string processing.