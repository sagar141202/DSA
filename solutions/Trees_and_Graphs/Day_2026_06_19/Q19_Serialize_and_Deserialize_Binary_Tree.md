# Serialize and Deserialize Binary Tree

## Problem Statement
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment. Deserialization is the reverse process, where the sequence of bits is converted back into a data structure or object. Given the root node of a binary tree, write a function to serialize the binary tree into a string, and another function to deserialize the string back into a binary tree. The serialized binary tree should be as compact as possible, and the deserialized binary tree should be the same as the original binary tree structure. For example, given the binary tree `1 / \ 2   3 / \   4   5`, the serialized string should be `"1,2,3,x,x,4,5,x,x,x,x"`.

## Approach
We will use a pre-order traversal to serialize the binary tree into a string, and then use the same traversal order to deserialize the string back into a binary tree. We will use 'x' to represent null nodes in the serialized string.

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
            oss << "x,";
        } else {
            oss << node->val << ",";
            serializeHelper(node->left, oss);
            serializeHelper(node->right, oss);
        }
    }

    TreeNode* deserializeHelper(istringstream& iss) {
        string val;
        getline(iss, val, ',');
        if (val == "x") {
            return NULL;
        } else {
            TreeNode* node = new TreeNode(stoi(val));
            node->left = deserializeHelper(iss);
            node->right = deserializeHelper(iss);
            return node;
        }
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
Output: "1,2,4,x,x,5,x,x,3,x,x"
```

## Key Takeaways
- Use pre-order traversal for serialization and deserialization.
- Represent null nodes with 'x' in the serialized string.
- Utilize ostringstream for efficient string construction during serialization.