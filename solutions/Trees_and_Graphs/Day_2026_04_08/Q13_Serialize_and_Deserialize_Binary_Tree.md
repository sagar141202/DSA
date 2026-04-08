# Serialize and Deserialize Binary Tree

## Problem Statement
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment. Deserialization is the reverse process, where the sequence of bits is converted back into a data structure or object. Given the root node of a binary tree, write a function to serialize it into a string, and another function to deserialize the string back into a binary tree. The binary tree node has the following definition: `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode(int x) : val(x), left(NULL), right(NULL) };`. The string should be encoded as `X,X,X,...` where `X` is a node's value, and `NULL` represents a null node. For example, the binary tree `1,2,3,null,null,4,5` represents the following structure: 
        1
       / \
      2   3
     / \
    4   5
    The function should be able to handle the serialization and deserialization of a binary tree of any size.

## Approach
We will use a depth-first search (DFS) approach to traverse the binary tree and serialize it into a string. The DFS traversal will be pre-order, meaning we visit the current node before its children. We will use a comma to separate the node values in the string. For deserialization, we will use a recursive approach to construct the binary tree from the serialized string.

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
        if (node) {
            oss << node->val << ",";
            serializeHelper(node->left, oss);
            serializeHelper(node->right, oss);
        } else {
            oss << "#,";
        }
    }

    TreeNode* deserializeHelper(istringstream& iss) {
        string val;
        getline(iss, val, ',');
        if (val == "#") {
            return nullptr;
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
Output: "1,2,4,5,3,"
Input: data = "1,2,3,null,null,4,5"
Output: [1,2,3,null,null,4,5]
```

## Key Takeaways
- The `serialize` function uses a pre-order DFS traversal to convert the binary tree into a string.
- The `deserialize` function uses a recursive approach to construct the binary tree from the serialized string.
- The `#` character is used to represent a null node in the serialized string.