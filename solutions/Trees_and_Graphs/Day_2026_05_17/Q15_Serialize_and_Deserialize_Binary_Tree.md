# Serialize and Deserialize Binary Tree

## Problem Statement
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment. Deserialization is the reverse process, where the sequence of bits is converted back into a data structure or object. Given the root node of a binary tree, write a function to serialize it into a string, and another function to deserialize the string back into a binary tree. The binary tree node has the following definition: `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode(int x) : val(x), left(NULL), NULL); }`. For example, the binary tree `1 / \ 2   3 / \ 4   5` can be serialized into the string `"1,2,4,X,X,3,5,X,X,X,X"`, where `X` represents a null node.

## Approach
We will use a recursive pre-order traversal to serialize the tree, and a recursive function to deserialize the string. The serialization function will append the value of each node to the string, followed by a comma, and append 'X' for null nodes. The deserialization function will split the string into a vector of strings, and use a recursive function to construct the binary tree.

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

    // Helper function for serialization
    void serializeHelper(TreeNode* node, ostringstream& oss) {
        if (node) {
            oss << node->val << ",";
            serializeHelper(node->left, oss);
            serializeHelper(node->right, oss);
        } else {
            oss << "X,";
        }
    }

    // Helper function for deserialization
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
- Use pre-order traversal to serialize the binary tree.
- Use a recursive function to deserialize the string back into a binary tree.
- Handle null nodes by appending 'X' to the serialized string.