# Serialize and Deserialize Binary Tree

## Problem Statement
Serialization is the process of converting a data structure into a linear format, such as a string, that can be stored or transmitted. Deserialization is the reverse process of reconstructing the original data structure from the serialized format. Given a binary tree, design an algorithm to serialize and deserialize it. The serialization of a binary tree is a string representation of the tree where each node is represented by its value followed by a comma, and null nodes are represented by 'X'. For example, the serialization of the following binary tree: 
      1
     / \
    2   3
       / \
      4   5
is "1,2,X,3,4,X,5,X,X,X". The deserialization of the string "1,2,X,3,4,X,5,X,X,X" should return the original binary tree.

## Approach
We can solve this problem by using a recursive approach to serialize and deserialize the binary tree. The idea is to perform a pre-order traversal of the tree, appending each node's value to the serialized string and appending 'X' for null nodes. For deserialization, we can reconstruct the tree by recursively creating nodes and assigning their left and right children based on the serialized string.

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
        if (!node) {
            oss << "X,";
            return;
        }
        oss << node->val << ",";
        serializeHelper(node->left, oss);
        serializeHelper(node->right, oss);
    }
    
    TreeNode* deserializeHelper(istringstream& iss) {
        string val;
        getline(iss, val, ',');
        if (val == "X") return nullptr;
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
Output: "1,2,X,3,4,X,5,X,X,X"
```

## Key Takeaways
- The serialization process involves performing a pre-order traversal of the binary tree and appending each node's value to the serialized string.
- The deserialization process involves recursively creating nodes and assigning their left and right children based on the serialized string.
- The time complexity of the solution is O(N), where N is the number of nodes in the binary tree, since each node is visited once during serialization and deserialization.