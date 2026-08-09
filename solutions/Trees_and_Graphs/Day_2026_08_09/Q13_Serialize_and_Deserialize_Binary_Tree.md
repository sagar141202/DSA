# Serialize and Deserialize Binary Tree

## Problem Statement
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment. Deserialization is the reverse process, where the sequence of bits is converted back into a data structure or object. Given the root of a binary tree, serialize it into a string, and then deserialize the string back into a binary tree. The serialized format should be a string of nodes separated by commas, where each node is represented as an empty node (`X`) or a node with its value and children. For example, the binary tree `root = [1,2,3,null,null,4,5]` is represented as a string `"1,2,X,X,3,4,X,X,5,X,X"`. The deserialized binary tree should be the same as the original binary tree.

## Approach
To solve this problem, we will use a recursive approach for serialization and deserialization. We will traverse the tree in a pre-order manner, adding each node's value to the serialized string. For deserialization, we will recursively construct the binary tree from the serialized string.

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
Input: root = [1,2,3,null,null,4,5]
Output: "1,2,X,X,3,4,X,X,5,X,X"
```

## Key Takeaways
- Use recursive approach to solve the problem.
- Serialize the binary tree in a pre-order manner.
- Deserialize the string back into a binary tree by recursively constructing the tree.