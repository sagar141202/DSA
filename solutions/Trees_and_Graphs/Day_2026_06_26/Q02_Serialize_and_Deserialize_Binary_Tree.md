# Serialize and Deserialize Binary Tree

## Problem Statement
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment. Deserialization is the reverse process, where the sequence of bits is converted back into an object. Given the root of a binary tree, serialize it into a string, and then deserialize the string back into a binary tree. The serialized format should be a string of values separated by commas, where each value represents the value of a node. If a node is null, it should be represented as "X". For example, given the binary tree `    1
   / \
  2   3
 / \
4   5`, the serialized string would be `"1,2,4,X,X,5,X,X,3,X,X"`. The deserialized binary tree should be identical to the original binary tree.

## Approach
We will use a recursive Depth-First Search (DFS) approach to serialize the binary tree, and then use a queue to deserialize the string back into a binary tree. The serialization process will traverse the tree in a pre-order manner, and the deserialization process will use a queue to reconstruct the tree level by level.

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

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream iss(data);
        return deserializeHelper(iss);
    }

    void serializeHelper(TreeNode* node, ostringstream& oss) {
        if (node == NULL) {
            oss << "X,";
        } else {
            oss << node->val << ",";
            serializeHelper(node->left, oss);
            serializeHelper(node->right, oss);
        }
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
Input: 
    1
   / \
  2   3
 / \
4   5
Output: "1,2,4,X,X,5,X,X,3,X,X"
```

## Key Takeaways
- Use a recursive DFS approach to serialize the binary tree.
- Use a queue to deserialize the string back into a binary tree.
- The serialized format should be a string of values separated by commas, where each value represents the value of a node.